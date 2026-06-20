# CareerPilot Architecture

## Goal

Provide personalized placement preparation using multiple collaborating AI agents.

---

## System Flow

User
↓
Orchestrator Agent
↓
Security Agent
↓
Resume Agent
DSA Agent
Interview Agent
Progress Agent
Scheduler Agent

---

## Agent Responsibilities

### Orchestrator Agent

Responsibilities:

- Intent detection
- Agent routing
- Response aggregation

---

### Security Agent

Responsibilities:

- Detect PII
- Mask sensitive information
- Detect prompt injection attacks

---

### Resume Agent

Inputs:

- Resume PDF
- Target Role

Outputs:

- Resume score
- Missing skills
- Suggestions

---

### DSA Agent

Inputs:

- Current skill level
- Target role

Outputs:

- Weekly roadmap
- Learning milestones

---

### Interview Agent

Inputs:

- Target role

Outputs:

- Interview preparation plan
- Mock questions

---

### Progress Agent

Inputs:

- Completed tasks

Outputs:

- Readiness score
- Analytics

---

### Scheduler Agent

Inputs:

- Roadmap

Outputs:

- Calendar events
- Study schedules

---

## External Integrations

Google Drive MCP

- Save reports

Google Calendar MCP

- Create events

GitHub MCP

- Analyze coding activity