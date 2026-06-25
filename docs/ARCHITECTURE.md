# CareerPilot AI – System Architecture

## Overview

CareerPilot AI is a production-style multi-agent career preparation assistant built using the **Google Agent Development Kit (ADK)**. It helps students prepare for placements by combining multiple specialized AI agents that collaborate through a central orchestrator.

The system provides resume analysis, DSA roadmaps, interview preparation, progress tracking, study scheduling, memory management, MCP integrations, and a security layer.

---

# Architecture Goals

The architecture is designed to achieve the following objectives:

* Modular multi-agent architecture
* Intelligent task routing
* Secure AI interactions
* Persistent user memory
* External system integrations
* Easy scalability
* Production-ready organization

---

# High-Level Architecture

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
      │          │         │          │          │          │
      └──────────┴─────────┴──────────┴──────────┴──────────┘
                          │
                          ▼
                     Tool Layer
                          │
         ┌────────────┬────────────┬─────────────┐
         ▼            ▼            ▼
     Memory Layer   MCP Layer   Security Layer
                          │
                          ▼
                    Final Response
```

---

# System Execution Flow

The application processes each request using the following pipeline:

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
Intent Detection
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
Response Generation
      │
      ▼
User
```

---

# Agent Responsibilities

## Orchestrator Agent

Responsibilities:

* Understand user intent
* Select the appropriate specialist agent
* Route requests
* Coordinate multi-agent execution
* Return a unified response

---

## Resume Agent

Responsibilities:

* Resume analysis
* Resume scoring
* Job matching
* Skill gap analysis
* Career recommendations
* Resume report generation

Primary Tools:

* Resume Analyzer
* Job Match Tool
* Skill Gap Roadmap
* Job Recommendation Tool

---

## DSA Agent

Responsibilities:

* Generate learning roadmaps
* Recommend coding problems
* Study planning
* Progress monitoring

Primary Tools:

* DSA Roadmap Tool
* Problem Recommendation Tool
* Study Schedule Tool

---

## Interview Agent

Responsibilities:

* Generate mock interviews
* Evaluate interview answers
* Company-specific interview preparation

Primary Tools:

* Mock Interview Tool
* Interview Feedback Tool
* Company Questions Tool

---

## Progress Agent

Responsibilities:

* Track learning progress
* Calculate completion percentage
* GitHub activity analysis
* Goal tracking

Primary Tools:

* Progress Tracker
* Goal Tracker
* GitHub Tools

---

## Scheduler Agent

Responsibilities:

* Study planning
* Reminder creation
* Calendar scheduling

Primary Tools:

* Reminder Tool
* Calendar Tool

---

## Security Agent

Responsibilities:

* Detect Prompt Injection
* Detect Jailbreak attempts
* Detect Personally Identifiable Information (PII)
* Resume sanitization
* Output validation

---

# Memory Layer

CareerPilot stores important user information across multiple specialized memory modules.

Modules include:

* Profile Store
* Skills Store
* Roadmap Store
* Interview Store

Benefits:

* Personalized responses
* Progress persistence
* Learning history
* Resume tracking

---

# MCP Integration Layer

CareerPilot integrates with external systems through Model Context Protocol (MCP).

Current Integrations:

## Google Drive MCP

Used for:

* Exporting reports
* Saving generated documents

---

## Google Calendar MCP

Used for:

* Study schedule creation
* Reminder management

---

## GitHub MCP

Used for:

* Repository statistics
* Recent commits
* Progress monitoring

---

# Security Architecture

Every request passes through a dedicated security layer before reaching AI agents.

Security Components:

* Prompt Injection Detector
* Jailbreak Detector
* PII Detector
* PII Masker
* Resume Sanitizer
* Output Validator

Security Benefits:

* Prevents malicious prompts
* Protects sensitive information
* Produces safer AI responses

---

# Tool Layer

The tool layer contains reusable business logic shared across multiple agents.

Examples include:

* Resume Analyzer
* Job Matcher
* DSA Roadmap Generator
* Interview Feedback
* Progress Tracker
* Report Export
* Reminder Manager

This separation keeps agent prompts simple while concentrating application logic in reusable tools.

---

# Runtime

CareerPilot uses the Google Agent Development Kit (ADK) runtime.

Runtime responsibilities include:

* Agent execution
* Session handling
* Multi-agent routing
* Tool invocation
* Artifact management
* Development UI support

---

# Benefits of the Architecture

The architecture provides:

* Modular design
* Easy maintenance
* Reusable components
* Secure AI interactions
* Multi-agent collaboration
* Production-ready organization
* Scalability for future agents and integrations

---

# Future Improvements

Potential future enhancements include:

* Real Google Drive API integration
* Real Google Calendar API integration
* GitHub REST API integration
* Persistent database-backed memory
* Authentication and user accounts
* Cloud deployment (Vertex AI Agent Engine or Cloud Run)
* Monitoring and observability
* Expanded evaluation benchmarks
