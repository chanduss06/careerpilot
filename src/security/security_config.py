"""
CareerPilot Security Configuration

This file contains global security settings and constants
used across the security layer.
"""

# -----------------------------
# Security Feature Flags
# -----------------------------

ENABLE_PII_MASKING = True
ENABLE_PROMPT_INJECTION_CHECK = True
ENABLE_JAILBREAK_CHECK = True
ENABLE_OUTPUT_VALIDATION = True
ENABLE_RESUME_SANITIZATION = True

# -----------------------------
# Detection Thresholds
# -----------------------------

MAX_PROMPT_LENGTH = 5000
MAX_RESUME_SIZE = 25000

# -----------------------------
# Logging
# -----------------------------

LOG_SECURITY_EVENTS = True

# -----------------------------
# Security Version
# -----------------------------

SECURITY_VERSION = "1.0.0"