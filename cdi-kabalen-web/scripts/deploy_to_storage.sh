#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="${ROOT_DIR}/artifacts/azure/env.prod"

if [[ ! -f "${ENV_FILE}" ]]; then
  echo "Environment file not found: ${ENV_FILE}" >&2
  exit 1
fi

# shellcheck disable=SC1090
source "${ENV_FILE}"

: "${AZURE_STORAGE_ACCOUNT:?AZURE_STORAGE_ACCOUNT is required}"
: "${AZURE_STATIC_CONTAINER:?AZURE_STATIC_CONTAINER is required}"

BUSINESS_IDENTIFIER="${CONTENT_BUSINESS:-kabalian}"

python3 "${ROOT_DIR}/scripts/build_variants.py" --business "${BUSINESS_IDENTIFIER}"

SOURCE_DIR="${ROOT_DIR}/build/azure/${BUSINESS_IDENTIFIER}"

if [[ ! -d "${SOURCE_DIR}" ]]; then
  echo "Expected Azure bundle not found: ${SOURCE_DIR}" >&2
  exit 1
fi

if [[ -n "${AZURE_SUBSCRIPTION_ID:-}" ]]; then
  az account set --subscription "${AZURE_SUBSCRIPTION_ID}"
fi

az storage blob upload-batch \
  --account-name "${AZURE_STORAGE_ACCOUNT}" \
  --destination "${AZURE_STATIC_CONTAINER}" \
  --source "${SOURCE_DIR}" \
  --overwrite

echo "Static site deployment completed."
