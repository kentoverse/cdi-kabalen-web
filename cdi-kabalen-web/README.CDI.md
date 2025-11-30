# CDI College – Web and Mobile Application Development Program

## Course: Fundamentals of Web Development (HTML5 & CSS)

---

### 👤 Student Information

| Name | Student ID | Program | Term | Campus | Date |
|------|-------------|----------|-------|---------|------|
| **Marc Cavdada** | **664408258** | Web and Mobile Application Development | Session 6–10 | CDI College | **Nov 30, 2025** |

---

### 📚 Coursework Summary

| Course | Assignment / Project | Date | Status / Link |
|--------|----------------------|------|----------------|
| Fundamentals of Web Development | **Assignment 1 – HTML Foundations** | Oct 25, 2025 | ✅ Completed |
| Fundamentals of Web Development | **Assignment 2 – CSS & Responsive Design** | Nov 30, 2025 | 🔗 [Live on Azure](https://ca-mcp-s3d6qmutzsu2w.mangopond-68601273.canadaeast.azurecontainerapps.io) |
| Fundamentals of Web Development | **Assignment 3 – Layouts, Forms & Media** | Dec 15, 2025 | 🔗 [Assignment 3 Site](https://appi-mcp-s3d6qmutzsu2w.azurewebsites.net/assignment3/index.html) |
| Fundamentals of Web Development | **Final Project – Kabalen Restaurant Website Redesign** | Dec 2025 | 🔗 [Live on Azure](https://kabalenstaticstore.z27.web.core.windows.net/) |
| JavaScript Fundamentals | **Next Project – Interactive Web App (Portfolio)** | Jan 2026 | 🧩 Planned |

---

## 🍽️ Final Project – Kabalen Restaurant Website Redesign

- **Course:** Fundamentals of Web Development (HTML5 & CSS)
- **Student:** Marc Cavdada
- **Term:** Session 10 Final Project
- **Due:** Session 15

### 📌 Project Overview

The final project involves selecting a local restaurant with an outdated or poorly structured website and redesigning it using **HTML5, CSS3, and JavaScript**, following all CDI College requirements.

#### Kabalen Toronto – Authentic Filipino Cuisine (Bathurst Area)

Kabalen serves traditional Filipino dishes and Kamayan-style dining. Its online presence lacks modern structure and responsiveness, making it an ideal candidate for a professional redesign.

### 🎯 Project Goals

- Create a modern, mobile-first layout
- Improve readability and navigation
- Build **6–11 HTML pages** using external CSS
- Use Flexbox + CSS Grid for layout
- Add multimedia and visual design elements
- Implement a working form with JavaScript validation
- Ensure HTML/CSS W3C validation
- Publish a fully accessible public version hosted on Azure

### 📄 Planned Page Structure (6–11 Pages)

1. **Home** – Hero banner, overview
2. **Menu** – Dish cards, images, prices
3. **Daily Specials** – Feed-style specials
4. **Gallery** – Food & Kamayan photos
5. **About Us** – Restaurant story
6. **Contact / Reservation Form** – JS validation
7. **Location & Hours** – Map embed
8. **Kamayan Feast** (optional)
9. **Catering Services** (optional)

### 🛠️ Technical Requirements Checklist

| Requirement | Status |
|------------|--------|
| Semantic HTML5 | ✔ |
| External CSS stylesheet | ✔ |
| Responsive design w/ media queries | ✔ |
| Consistent navigation across pages | ✔ |
| Tables / Lists included | ✔ |
| Image gallery & multimedia | ✔ |
| Contact form (3 inputs min.) | ✔ |
| JavaScript interactivity | ✔ |
| CSS Grid & Flexbox | ✔ |
| W3C validation | ✔ |
| Minimum 6 pages | ✔ |

### 🎨 Design Approach

The design uses a clean, card-based interface inspired by food delivery and modern restaurant websites.

Project highlights:

- Clear typography
- Generous white space for readability
- High-quality Filipino dish imagery
- Layout grids for menu and gallery
- Color palette inspired by Filipino culture

The design is both modern and fully aligned with CDI’s academic expectations.

---

## 🌐 Live Project Deployment

The static website is hosted on **Azure Storage Static Web Hosting**.

### 🔗 Final Project URL

🔗 [kabalenstaticstore.z27.web.core.windows.net](https://kabalenstaticstore.z27.web.core.windows.net/)

#### Latest Production Sync

- **Deployed:** Nov 30, 2025 @ 11:46 UTC via `scripts/build_variants.py` + `scripts/deploy_to_storage.sh`
- **Bundle:** `build/azure/kabalian`
- **Verification:** `curl -I https://kabalenstaticstore.z27.web.core.windows.net/` → `HTTP/1.1 200`

### 📁 Project Structure

```text
cdi-kabalen-web/
├── index.html
├── menu.html
├── specials.html
├── gallery.html
├── about.html
├── contact.html
└── assets/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── form.js
    └── images/
```

---

## 📘 Milestones

### Milestone 1 – Planning & Analysis

Includes:

- Website goals
- Page plan
- Multimedia plan
- Content plan
- JavaScript behavior
- Hosting strategy
- Design considerations
- Sitemap outline

### Milestone 2 – Sitemap & Wireframes

Delivered using ASCII wireframes and mobile-first planning.

---

## 🚀 Future Development (Beyond CDI Scope)

After grading, the project may expand into:

- FastAPI backend
- SQLite database
- Admin dashboard for menu updates
- Dynamic content rendering
- BOTWorks app integration

These enhancements are future learning goals, not part of the CDI submission.

---

## 🆕 Latest Development Snapshot (Nov 30, 2025)

- **Repository Sync:** `main` branch pushed to both `origin` and `cdi-origin`.
- **Static Bundles:** Regenerated Azure/GCP artifacts with `python3 scripts/build_variants.py --business kabalian`.
- **Azure Publish:** Synced `build/azure/kabalian` to Azure Storage using `CONTENT_BUSINESS=kabalian ./scripts/deploy_to_storage.sh`.
- **Validation:** Confirmed deployment with `curl -I https://kabalenstaticstore.z27.web.core.windows.net/` (HTTP 200).
- **Pending Artifact:** `final-project.zip` remains local for future packaging; excluded from commits and deploys.

---

## 🗂️ CSV-Driven Content Workflow

The next evolution of the Kabalen site introduces a CSV-powered content flow so non-technical contributors can revise copy, highlight dishes, and manage gallery images without editing HTML.

### Editing Content

- Open `content/content-template.csv` in Excel, Numbers, or Google Sheets.
- Each row represents a section or card on a specific page.
- Update the columns:
  - **business**: brand identifier (e.g., `kabalian`); leave blank to share across all brands.
  - **page**: logical page key (e.g., `index`, `menu`).
  - **section**: stable identifier for anchors or styling hooks.
  - **title / subtitle / content**: textual copy.
  - **image**: relative path under `assets/images/`.
  - **display**: set to `true` to publish the block, `false` to hide it.
  - **order**: lowest numbers render first.
  - **content_type**: semantic hint (e.g., `hero`, `card`, `gallery-item`).
  - **filename**: target HTML file (defaults to `<page>.html` when blank).

### Generating Pages

- Save the CSV.
- Run the generator from the project root (the `--business` flag is optional when previewing a single brand):

  ```bash
  python3 generate_pages.py content/content-template.csv --business kabalian --output generated-pages
  ```

- The helper script `scripts/build_variants.py` automates both Azure and GCP builds in one pass:

  ```bash
  python3 scripts/build_variants.py --business kabalian
  ```

- Generated HTML bundles land under `build/azure/<business>` and `build/gcp/<business>` and contain `content.json` plus the copied `assets/` directory.

### Image Slot Placeholders

- Pages with gallery-style content auto-fill up to 10 image slots.
- Leave unused slots blank in the CSV; the generator inserts accessible placeholders.
- Upload new images to `assets/images/` and reference the path in the CSV when ready.

This workflow enables a light CMS experience while the project transitions toward a fully dynamic FastAPI stack.

---

## ⚙️ FastAPI Content Service

The `/api` package introduces a FastAPI microservice that mirrors the CSV authoring model for downstream consumers.

### Running the API locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn api.main:app --reload
```

- `GET /healthz` → basic uptime probe.
- `GET /pages` → returns the full sitemap with sections grouped by HTML filename.
- `GET /pages/{page}` → fetch the sections for a specific page (`index` or `index.html`).
- `GET /pages/{page}/sections/{section}` → pull a single section payload, useful for CMS previews.

The API lazily caches `content/content-template.csv` and automatically reloads when the file timestamp changes.

---

## 🔁 Build & Deploy Pipeline

### 1. Generate Azure + GCP bundles

```bash
python3 scripts/build_variants.py --business kabalian
```

Artifacts:

- `build/azure/kabalian` → HTML + assets + `content.json` for Azure Static Website.
- `build/gcp/kabalian` → identical bundle for Firebase Hosting.

### 2. Publish to Azure Static Web Apps (Blob `$web`)

```bash
CONTENT_BUSINESS=kabalian ./scripts/deploy_to_storage.sh
```

Requirements:

- Azure CLI authenticated with access to subscription `17564e57-40b0-434d-b566-604c60cee028`.
- `artifacts/azure/env.prod` populated with storage account metadata (`CONTENT_BUSINESS` defaults to `kabalian`).

The script rebuilds the bundles if necessary, optionally switches subscriptions, and syncs the Azure bundle into the `$web` container of `kabalenstaticstore`.

### 3. Publish to GCP Firebase Hosting

```bash
CONTENT_BUSINESS=kabalian FIREBASE_PROJECT=<gcp-project-id> ./scripts/deploy_to_firebase.sh
```

Expectations:

- Firebase CLI (`firebase-tools`) installed and authenticated for the target project.
- The script regenerates `firebase.json` so the hosting `public` path matches `build/gcp/<business>` before calling `firebase deploy --only hosting`.
- Authentication can be supplied with a service-account JSON:

  ```bash
  export GOOGLE_APPLICATION_CREDENTIALS=/absolute/path/firebase-adminsdk.json
  firebase login:ci --no-localhost
  ```

- Alternatively, activate the service account with `gcloud auth activate-service-account --key-file "$GOOGLE_APPLICATION_CREDENTIALS"` prior to running the deploy script.

---

## 📘 Assignment 3 – Session 10

- **Course:** Fundamentals of Web Development
- **Student:** Marc Cavdada
- **Date:** December 2025

### Overview

This assignment introduced layout, multimedia, forms, and interactivity.

### Live Site

🔗 [Assignment 3 Live Site](https://appi-mcp-s3d6qmutzsu2w.azurewebsites.net/assignment3/index.html)

### Objectives

- Flexbox & CSS Grid
- Multimedia integration
- Forms
- Basic JavaScript

---

## 🚀 Next Steps

Upcoming topics for backend development:

- Python (Flask, FastAPI)
- SQLite data modeling
- API development
- Server-side rendering

---

## 🧱 Next Build Plan – CSV to FastAPI Bridge

The upcoming build focuses on turning the CSV authoring workflow into a repeatable build pipeline.

### Sprint Goals

- Ship a FastAPI microservice that reads the CSV and serves JSON endpoints for each page.
- Add a build script that transforms CSV → JSON → Static HTML so non-technical editors only touch `content/content-template.csv`.
- Automate Azure Blob deployments by bundling the generator run and `az storage blob upload-batch` commands into a single task.
- Stand up a GitHub Actions workflow that runs the generator, executes `deploy_to_storage.sh` with federated credentials, and (optionally) triggers Firebase hosting sync.
- Add a lightweight uptime probe (scheduled workflow or Azure Function) that records the live site `Last-Modified` header for monitoring.

### Deliverables

- `/api` folder with FastAPI app, Pydantic models, and CSV adapter.
- `package.json` or `pyproject.toml` entries to run `python3 generate_pages.py` before deployment.
- GitHub Actions workflow artifacts that publish generated HTML to `$web`, invalidate cached assets if needed, and capture deployment metadata.

### Acceptance Criteria

- Running one command should regenerate HTML, produce JSON previews, and push to Azure when credentials are provided.
- Documentation includes a flow diagram showing CSV editors how updates propagate to production.
- Tests cover CSV parsing edge cases (missing columns, hidden sections, image placeholders).
- CI pipeline posts deployment success/failure status and persists the latest live URL/etag in the workflow summary.

This plan keeps the CSV-first governance intact while laying the groundwork for a FastAPI-powered CMS experience.

---

### 📄 End of Document

⸻


