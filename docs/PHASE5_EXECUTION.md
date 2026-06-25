# Phase 5 – ADK Execution Pipeline

## Objective

Phase 5 transforms CareerPilot AI from a collection of independent AI agents into a complete multi-agent application powered by the Google Agent Development Kit (ADK).

This phase focuses on orchestrating agent execution, organizing runtime components, integrating security, and enabling end-to-end execution through the ADK runtime.

---

# Phase 5 Goals

The primary objectives of this phase were:

* Establish a runtime layer
* Improve multi-agent orchestration
* Connect the application to Google ADK
* Support session-based execution
* Integrate the security layer
* Prepare memory and MCP integration
* Enable complete end-to-end execution

---

# Components Added

## Runtime Package

A dedicated runtime package was introduced.

```text
src/runtime/
├── __init__.py
├── execution_context.py
├── response.py
├── runner.py
└── session_manager.py
```

Responsibilities include:

* Runtime coordination
* Session metadata
* Execution context
* Standardized runtime responses

---

## Enhanced Orchestrator

The root ADK agent was expanded to support all specialist agents.

Connected agents:

* Resume Agent
* DSA Agent
* Interview Agent
* Progress Agent
* Scheduler Agent
* Security Agent

The orchestrator is responsible for understanding user intent and delegating requests to the appropriate specialist.

---

# Execution Flow

Every request follows the pipeline below.

```text
User Request
      │
      ▼
Google ADK Runtime
      │
      ▼
CareerPilot Orchestrator
      │
      ▼
Specialized Agent
      │
      ▼
Tool Execution
      │
      ▼
Memory / MCP
      │
      ▼
Response
```

---

# Multi-Agent Communication

The orchestrator routes requests to specialist agents based on intent.

Example routing:

| User Request       | Selected Agent  |
| ------------------ | --------------- |
| Resume Review      | Resume Agent    |
| Skill Gap Analysis | Resume Agent    |
| DSA Roadmap        | DSA Agent       |
| Coding Preparation | DSA Agent       |
| Mock Interview     | Interview Agent |
| Company Questions  | Interview Agent |
| Progress Report    | Progress Agent  |
| Study Schedule     | Scheduler Agent |
| Security Analysis  | Security Agent  |

This architecture allows agents to specialize while keeping the orchestrator lightweight.

---

# Runtime Components

## CareerPilotRunner

Acts as the application entry point.

Responsibilities:

* Initialize runtime
* Create execution context
* Coordinate request execution

---

## SessionManager

Responsible for creating runtime session metadata.

Current implementation uses lightweight session tracking while leveraging the Google ADK runtime.

---

## ExecutionContext

Stores runtime metadata including:

* Session ID
* User ID
* Request metadata

---

## RuntimeResponse

Provides a standardized response object for runtime operations.

---

# Security Integration

CareerPilot includes a dedicated security pipeline introduced during Phase 4.

Security components:

* Prompt Injection Detector
* Jailbreak Detector
* PII Detector
* PII Masker
* Resume Sanitizer
* Output Validator

The security layer validates user input and model output before information is processed or returned.

---

# Memory Integration

The application uses modular memory stores.

Current memory modules include:

* Profile Store
* Skills Store
* Roadmap Store
* Interview Store

These modules support personalized learning experiences and progress persistence.

---

# MCP Integration

CareerPilot integrates external services using the Model Context Protocol (MCP).

Current integrations include:

## Google Drive MCP

Used to save generated reports.

---

## Google Calendar MCP

Used to generate study schedules and reminders.

---

## GitHub MCP

Used to retrieve repository statistics and recent commits.

---

# Runtime Advantages

The runtime architecture provides:

* Separation of concerns
* Modular execution
* Easy maintenance
* Scalability
* Cleaner testing
* Improved organization

---

# Testing

The project includes automated testing using **pytest**.

Areas covered include:

* Security layer
* Memory layer
* MCP modules
* Runtime components
* Tool functionality

GitHub Actions automatically executes the test suite on every push.

---

# Results

By the end of Phase 5, CareerPilot AI supports:

* Google ADK execution
* Multi-agent orchestration
* Tool-based execution
* Runtime abstraction
* Security validation
* Memory management
* MCP integrations
* End-to-end workflow

---

# Future Improvements

Future work may include:

* Persistent database-backed sessions
* Real Google Drive API integration
* Real Google Calendar API integration
* GitHub REST API integration
* Cloud deployment
* Authentication and user accounts
* Advanced evaluation benchmarks
* Observability and monitoring

---

# Phase 5 Summary

Phase 5 completes the transition from a set of individual AI agents into a structured, production-style multi-agent application.

The resulting architecture is modular, extensible, secure, and suitable for further development, portfolio presentation, and technical interviews.
