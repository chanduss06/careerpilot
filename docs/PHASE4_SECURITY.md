# CareerPilot – Phase 4 Security Layer

## Overview

Phase 4 introduces a production-inspired security layer for CareerPilot.

The goal is to protect user data before it reaches AI agents and to prevent sensitive information from being returned in model responses.

The security layer is modular, reusable, and independently testable.

---

# Security Architecture

```
User
   │
   ▼
SecureAgentRunner
   │
   ▼
SecurityMiddleware
   │
   ├── PromptInjectionDetector
   ├── JailbreakDetector
   ├── ResumeSanitizer
   │      ├── Normalize Resume
   │      └── Mask PII
   ├── PIIDetector
   └── OutputValidator
   │
   ▼
CareerPilot Agent
   │
   ▼
LLM
   │
   ▼
Output Validation
   │
   ▼
User
```

---

# Components

## PIIDetector

Detects sensitive information including

- Email addresses
- Phone numbers
- Aadhaar numbers
- PAN numbers
- GitHub URLs
- LinkedIn URLs
- IP addresses
- Credit card numbers

---

## PIIMasker

Masks detected information while preserving useful context.

Examples

```
john@gmail.com

↓

********@gmail.com
```

```
9876543210

↓

******3210
```

---

## PromptInjectionDetector

Detects attempts such as

- Ignore previous instructions
- Reveal system prompt
- Repeat everything above
- Role override attacks
- Policy bypass attempts

---

## JailbreakDetector

Detects jailbreak attempts including

- Developer Mode
- DAN Mode
- Roleplay attacks
- System override
- Malicious capability requests

---

## ResumeSanitizer

Prepares resumes before analysis.

Functions include

- Whitespace normalization
- Blank line cleanup
- PII masking

---

## OutputValidator

Detects sensitive information leaving the system.

Examples include

- API Keys
- Secret Tokens
- Passwords
- Private Keys
- System Prompt leakage
- Environment Variables

---

## SecurityMiddleware

Acts as the central security pipeline.

Responsibilities

- Validate user input
- Detect prompt injection
- Detect jailbreak attempts
- Sanitize resumes
- Generate security reports
- Validate model output

---

## SecureAgentRunner

Framework-independent wrapper around CareerPilot agents.

Provides

- Input validation
- Output validation
- Centralized security

---

# Testing

Phase 4 includes automated tests.

Current coverage

- test_pii.py
- test_prompt_injection.py
- test_jailbreak.py
- test_output_validator.py
- test_middleware.py
- test_secure_agent_runner.py

Result

```
28 Tests Passed
```

---

# Folder Structure

```
src/security/

base_detector.py
security_config.py
security_rules.py
security_response.py
pii_detector.py
pii_masker.py
prompt_injection.py
jailbreak_detector.py
resume_sanitizer.py
output_validator.py
security_middleware.py
secure_agent_runner.py
```

---

# Design Principles

The security layer follows

- Separation of concerns
- Modular architecture
- Reusable components
- Centralized middleware
- Automated testing
- Framework-independent execution

---

# Future Improvements

Future enhancements may include

- ML-based prompt injection detection
- OCR resume sanitization
- Secrets scanning
- Toxicity detection
- SQL injection detection
- XSS detection
- Security dashboards
- Monitoring and audit logs

---

# Phase Summary

Phase 4 successfully adds a complete security layer to CareerPilot.

Features delivered

- PII Detection
- PII Masking
- Prompt Injection Detection
- Jailbreak Detection
- Resume Sanitization
- Output Validation
- Security Middleware
- Secure Agent Runner
- Automated Testing