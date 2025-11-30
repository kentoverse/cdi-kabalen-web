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

## 🗂️ CSV-Driven Content Workflow

The next evolution of the Kabalen site introduces a CSV-powered content flow so non-technical contributors can revise copy, highlight dishes, and manage gallery images without editing HTML.

### Editing Content

- Open `content/content-template.csv` in Excel, Numbers, or Google Sheets.
- Each row represents a section or card on a specific page.
- Update the columns:
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
- Run the generator from the project root:

  ```bash
  python3 generate_pages.py content/content-template.csv --output generated-pages
  ```

- Updated HTML files appear in `generated-pages/` for review before publishing.
- Copy approved files into the root directory (or adjust deployment to pull from `generated-pages/`).

### Image Slot Placeholders

- Pages with gallery-style content auto-fill up to 10 image slots.
- Leave unused slots blank in the CSV; the generator inserts accessible placeholders.
- Upload new images to `assets/images/` and reference the path in the CSV when ready.

This workflow enables a light CMS experience while the project transitions toward a fully dynamic FastAPI stack.

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

### 📄 End of Document

⸻


