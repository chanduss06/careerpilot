# 🚀 CareerPilot AI

> **An AI-powered Multi-Agent Career Preparation Platform built with Google Agent Development Kit (ADK).**

CareerPilot AI is a production-style multi-agent system that helps students prepare for software engineering placements by combining specialized AI agents for resume analysis, DSA learning, interview preparation, progress tracking, and study scheduling.

The project demonstrates modern AI engineering concepts including **Google ADK**, **Multi-Agent Systems**, **Tool Calling**, **Memory Management**, **Model Context Protocol (MCP)**, **Security Middleware**, **Automated Testing**, and **CI/CD**.

---

# 📌 Features

## 🤖 Multi-Agent Architecture

* Central Orchestrator Agent
* Resume Analysis Agent
* DSA Roadmap Agent
* Interview Preparation Agent
* Progress Tracking Agent
* Scheduler Agent
* Security Agent

---

## 📄 Resume Intelligence

* Resume Review
* Resume Scoring
* Job Match Analysis
* Skill Gap Detection
* Career Recommendations
* Report Generation

---

## 💻 DSA Learning

* Personalized Learning Roadmaps
* Topic-wise Planning
* Weekly Study Plans
* Coding Preparation Guidance

---

## 🎯 Interview Preparation

* Mock Interview Questions
* Company-specific Questions
* Interview Answer Evaluation
* Interview Preparation Guidance

---

## 📊 Progress Tracking

* Learning Progress
* Goal Tracking
* GitHub Activity Summary
* Readiness Analytics

---

## 📅 Study Scheduler

* Study Planning
* Reminder Creation
* Calendar Event Generation

---

## 🛡️ Security Layer

* Prompt Injection Detection
* Jailbreak Detection
* Personally Identifiable Information (PII) Detection
* Resume Sanitization
* Output Validation

---

## 🧠 Memory Layer

* Profile Memory
* Skills Memory
* Roadmap Progress
* Interview History

---

## 🔗 MCP Integrations

Current simulated integrations include:

* Google Drive MCP
* Google Calendar MCP
* GitHub MCP

---

# 🏗️ Architecture

```text
                        User
                          │
                          ▼
                 Google ADK Runtime
                          │
                          ▼
              CareerPilot Orchestrator
                          │
      ┌──────────┬─────────┬──────────┬──────────┬──────────┐
      ▼          ▼         ▼          ▼          ▼          ▼
 Resume Agent  DSA Agent Interview Progress Scheduler Security
                             Agent      Agent     Agent    Agent
                          │
                          ▼
                     Tool Layer
                          │
            Memory + MCP + Security
                          │
                          ▼
                    Final Response
```

---

# 📂 Project Structure

```text
careerpilot/
│
├── careerpilot_agent/
├── src/
│   ├── tools/
│   ├── memory/
│   ├── security/
│   ├── mcp/
│   └── runtime/
│
├── tests/
├── docs/
├── reports/
├── calendar/
├── .github/
├── pyproject.toml
└── README.md
```

---

# 🛠️ Technology Stack

* Python 3.11+
* Google Agent Development Kit (ADK)
* Gemini 2.5 Flash
* Pytest
* GitHub Actions
* Model Context Protocol (MCP)
* Git

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/chanduss06/careerpilot.git
cd careerpilot
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Start the ADK Development Server

```bash
adk web
```

Open:

```text
http://127.0.0.1:8000
```

Select:

```
careerpilot_agent
```

---

# 🧪 Example Prompts

### Resume Analysis

```
Review my resume and identify missing skills for a Python Backend Developer role.
```

---

### DSA Roadmap

```
Create a 2-month DSA roadmap for Software Engineering interviews.
```

---

### Interview Preparation

```
Generate mock interview questions for Google Software Engineer.
```

---

### Progress Tracking

```
Show my current learning progress.
```

---

### Study Schedule

```
Create a Dynamic Programming study schedule for this week.
```

---

# 📸 Screenshots

Project screenshots are available in:

```
docs/screenshots/
```

Suggested screenshots:

* ADK Development UI
* Resume Agent
* DSA Agent
* Interview Agent
* Progress Agent
* Scheduler Agent
* Trace View

---

# 📖 Documentation

Detailed documentation is available in the `docs/` directory.

* PRD
* Architecture
* Project Structure
* Demo Guide
* Evaluation Plan
* Phase Summaries
* Security Documentation
* Phase 5 Execution

---

# 🧪 Testing

Run all automated tests:

```bash
pytest
```

Continuous Integration is configured using **GitHub Actions**.

---

# 🔮 Future Improvements

* Google Drive API Integration
* Google Calendar API Integration
* GitHub REST API
* Persistent Database-backed Memory
* Authentication & User Accounts
* Cloud Deployment (Cloud Run / Vertex AI)
* Monitoring & Logging
* Expanded Evaluation Benchmarks

---

# 👨‍💻 Author

**Chandra Shekar Chegondi**

B.Tech – Computer Science & Engineering

CMR College of Engineering & Technology

GitHub: https://github.com/chanduss06

---

# ⭐ Acknowledgements

* Google Agent Development Kit (ADK)
* Google Gemini
* Kaggle 5-Day Gen AI Intensive Course
* Open-source Python Community

---

## 📄 License

This project is developed for educational and portfolio purposes.
