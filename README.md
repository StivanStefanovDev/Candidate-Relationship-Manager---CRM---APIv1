# 🎯 Candidate Relationship Manager (CRM) API

A lightweight, API-first backend system for recruiters to track, manage, and engage with job candidates—built using C# and ASP.NET Core.

---

## 💼 Problem

Modern recruiters juggle dozens of candidates, job roles, and interview stages using bloated ATS systems, spreadsheets, or sticky notes. This leads to lost follow-ups, inconsistent feedback, and poor candidate experiences.

**This project solves that** by providing a focused backend system to:

- Track candidates per role
- Log interview stages and feedback
- Get reminded to follow up
- View insights and status at a glance

---

## ✅ Key Features

### 👤 Candidates

- Full profile with resume, contact info, tags, and status
- Attach to one or more job positions
- Notes from recruiter or team members

### 💼 Job Positions

- Title, description, location (remote/on-site)
- Track all related candidates
- Hiring status (Open, Closed, Paused)

### 📆 Interview Stages

- Structured interview pipeline per candidate
- Stage type, date, interviewer, feedback

### 🔔 Reminders

- Automatic or manual follow-up reminders
- Prevent candidates from slipping through the cracks

### 📊 Analytics (Basic)

- Candidates per job
- Conversion rates (Applied → Interview → Offer)
- Time spent in pipeline

---

## 🧱 Project Structure (Planned)

- `Domain/` – Core entities (Candidate, Job, InterviewStage)
- `Application/` – Services, interfaces, business logic
- `Infrastructure/` – EF Core, database setup, background jobs
- `API/` – Controllers, DTOs, endpoints, middleware
- `Tests/` – Unit and integration tests

Follows Clean Architecture principles.

---

## 🛠️ Tech Stack

- **C# + ASP.NET Core 8**
- **Entity Framework Core** (PostgreSQL or SQLite)
- **JWT Authentication**
- **MediatR** (CQRS-style commands/queries)
- **FluentValidation** (request validation)
- **Serilog** (structured logging)
- **Hangfire** or **Quartz.NET** (background reminders)
- **Swagger/OpenAPI** for docs
- **xUnit + Moq** for testing

---

## 🚀 Possible Extensions

- Email integration (e.g. follow-up emails, interview reminders)
- Resume parsing (via 3rd-party API or simple metadata)
- Shareable candidate profiles (public read-only tokens)
- Admin/team accounts with role-based access

---

## 👀 Who Is This For?

- **Recruiters** tired of bulky, bloated ATS tools
- **Engineering managers** who want visibility on pipeline
- **Developers** building clean, real-world C# backends

---

## 📂 Status

🧠 Planning phase  
✅ Architecture being mapped  
📌 First milestone: User Auth + Job + Candidate APIs

---

## 📣 Contributions / Ideas

This is an open-ended system—PRs and feature suggestions are welcome, especially from recruiters or hiring managers who want something better.

---
