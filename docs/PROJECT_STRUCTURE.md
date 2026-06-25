# CareerPilot AI – Project Structure

## Overview

CareerPilot AI follows a modular, production-style project structure. Each directory has a single responsibility, making the codebase easier to maintain, extend, and test.

---

# Root Directory

```text
careerpilot/
│
├── careerpilot_agent/
├── src/
├── docs/
├── tests/
├── reports/
├── calendar/
├── .github/
├── .env
├── pyproject.toml
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Folder Descriptions

## careerpilot_agent/

Contains the Google ADK agents that power the application.

Files include:

* `agent.py` – Root orchestrator agent
* `resume_agent.py`
* `dsa_agent.py`
* `interview_agent.py`
* `progress_agent.py`
* `scheduler_agent.py`
* `security_agent.py`

Responsibilities:

* Multi-agent orchestration
* Intent routing
* Agent specialization
* Tool invocation

---

## src/

Contains the application's core implementation.

```text
src/
├── tools/
├── memory/
├── mcp/
├── security/
├── runtime/
├── config/
└── agents/
```

---

## src/tools/

Reusable business logic shared by agents.

Examples:

* Resume analysis
* Job matching
* DSA roadmap generation
* Interview feedback
* Progress tracking
* Report exporting
* Study scheduling
* Calendar management

Keeping business logic inside tools allows agents to remain lightweight and focused.

---

## src/memory/

Stores user-specific learning information.

Modules include:

* Profile Store
* Skills Store
* Roadmap Store
* Interview Store

Responsibilities:

* Save learning progress
* Track completed topics
* Maintain interview history
* Store user profile data

---

## src/security/

Implements the application's security layer.

Components:

* PII Detector
* PII Masker
* Prompt Injection Detector
* Jailbreak Detector
* Resume Sanitizer
* Output Validator
* Security Middleware
* Secure Agent Runner

Responsibilities:

* Secure user input
* Protect sensitive data
* Validate model output

---

## src/mcp/

Contains Model Context Protocol (MCP) integrations.

Current integrations:

* Google Drive MCP
* Google Calendar MCP
* GitHub MCP

Responsibilities:

* Save reports
* Create study schedules
* Access repository information

---

## src/runtime/

Contains runtime abstractions used by the application.

Components include:

* Session Manager
* Execution Context
* Runtime Response
* CareerPilot Runner

Responsibilities:

* Runtime coordination
* Session metadata
* Execution flow

---

## src/config/

Stores project configuration files and shared settings.

---

## src/agents/

Reserved for future expansion of internal agent modules and shared agent utilities.

---

## docs/

Contains all project documentation.

Files include:

* PRD
* Architecture
* Phase summaries
* Demo guide
* Evaluation documentation
* Project structure
* Screenshots

---

## tests/

Contains automated tests for the project.

Examples:

* Security tests
* Memory tests
* MCP tests
* Runtime tests
* Tool tests

The project uses **pytest** and GitHub Actions for automated testing.

---

## reports/

Stores generated reports.

Examples:

* Resume reports
* Progress reports

This directory currently simulates Google Drive storage through the MCP layer.

---

## calendar/

Stores generated calendar events for the simulated Google Calendar integration.

---

## .github/workflows/

Contains CI/CD workflows.

Current workflow:

* Run pytest automatically on every push

---

# Design Principles

The project follows several software engineering principles:

* Separation of concerns
* Modular architecture
* Reusable business logic
* Production-ready folder organization
* Test-driven development
* Scalable multi-agent design

---

# Technology Stack

* Python 3.11+
* Google Agent Development Kit (ADK)
* Gemini 2.5 Flash
* Pytest
* GitHub Actions
* Model Context Protocol (MCP)

---

# Future Expansion

The current structure allows future additions such as:

* Authentication
* Cloud deployment
* Database-backed memory
* Additional AI agents
* Real Google API integrations
* Monitoring and logging

The modular organization ensures new functionality can be added without major restructuring.
