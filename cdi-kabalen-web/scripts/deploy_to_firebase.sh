#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUSINESS_IDENTIFIER="${CONTENT_BUSINESS:-kabalian}"
FIREBASE_PUBLIC="build/gcp/${BUSINESS_IDENTIFIER}"
FIREBASE_CONFIG="${ROOT_DIR}/firebase.json"

: "${FIREBASE_PROJECT:?FIREBASE_PROJECT environment variable is required}"

python3 "${ROOT_DIR}/scripts/build_variants.py" --business "${BUSINESS_IDENTIFIER}"

if [[ ! -d "${ROOT_DIR}/${FIREBASE_PUBLIC}" ]]; then
  echo "Expected Firebase bundle not found: ${ROOT_DIR}/${FIREBASE_PUBLIC}" >&2
  exit 1
fi

if ! command -v firebase >/dev/null 2>&1; then
  echo "firebase CLI is required. Install with 'npm install -g firebase-tools'." >&2
  exit 1
fi

cat >"${FIREBASE_CONFIG}" <<EOF
{
  "hosting": {
    "public": "${FIREBASE_PUBLIC}",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ]
  }
}
EOF

( cd "${ROOT_DIR}" && firebase deploy --only hosting ${FIREBASE_PROJECT:+--project "${FIREBASE_PROJECT}"} )

echo "Firebase hosting deployment completed."
