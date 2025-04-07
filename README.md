# 🎯 Candidate Relationship Manager (CRM) API

A clean, API-first backend system to help recruiters organize and manage their candidate pipelines—built with **Python** and **Django**.

---

## 💼 The Problem

Recruiters often have to manage dozens of candidates across multiple job openings using spreadsheets, inboxes, or overly complex applicant tracking systems (ATS). It’s messy, hard to follow up, and easy to lose track of good candidates.

This project aims to simplify that process by providing a focused backend system to:

- Track candidates per job position
- Manage interview stages and feedback
- Set reminders for follow-ups
- Quickly get a snapshot of candidate status and pipeline health

---

## ✅ Key Features

### 👤 Candidates

- Store candidate profiles with resume links, contact info, and status
- Assign candidates to one or more job positions
- Add notes or tags for easy filtering

### 💼 Job Positions

- Create and manage job postings (title, description, location)
- View all candidates linked to a job
- Mark roles as open, closed, or paused

### 📆 Interview Stages

- Track each candidate's interview progress
- Record stage type, date, interviewer name, and feedback

### 🔔 Reminders

- Set follow-up reminders to avoid ghosting good candidates
- Optional email or dashboard-based notifications

### 📊 Basic Analytics

- See how many candidates are in each stage
- Track conversion rates and drop-offs
- Understand average time spent in the pipeline

---

## 🧱 Planned Structure

We'll follow Django best practices with a modular app design:

- `accounts/` – Authentication, user management
- `jobs/` – Job positions and their metadata
- `candidates/` – Candidate profiles, attachments, tagging
- `interviews/` – Stages, scheduling, feedback
- `reminders/` – Follow-up logic (background tasks)
- `api/` – DRF views, serializers, routers
- `tests/` – Unit and integration test cases

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **Django 5.0**
- **Django REST Framework (DRF)** – API endpoints
- **PostgreSQL** – Primary database
- **Simple JWT** – Authentication
- **Celery + Redis** – Background jobs (for reminders)
- **pytest** – Testing
- **drf-spectacular** – OpenAPI/Swagger docs

---

## 🚀 Possible Extensions

- Resume upload and parsing
- Email integration for follow-ups or outreach
- Shareable candidate summaries (with access tokens)
- Multi-user teams and role-based permissions

---

## 👀 Who This Is For

- **Recruiters** who want a clean, focused way to manage pipelines
- **Hiring teams** looking for better candidate visibility
- **Developers** wanting to demonstrate Django API design, background jobs, and multi-entity systems

---

## 📂 Project Status

🧠 Planning and architecture  
✅ Core models and APIs scoped  
📌 First milestone: User Auth + Jobs + Candidates + Interview Stages

---

## 💬 Contributing & Feedback

This is a work-in-progress. If you're a recruiter, hiring manager, or dev with ideas for making it better, feel free to open an issue or pull request. Your feedback is welcome!

---
