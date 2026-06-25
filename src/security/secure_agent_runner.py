"""
CareerPilot Secure Agent Runner

Wraps ADK agents with the CareerPilot
Security Middleware.

Phase 4
"""

from typing import Any

from src.security.security_middleware import SecurityMiddleware


class SecureAgentRunner:
    """
    Executes an agent through the
    security pipeline.
    """

    def __init__(self):

        self.middleware = SecurityMiddleware()

    def validate_input(self, user_input: str) -> dict:
        """
        Validate incoming user input.
        """

        return self.middleware.inspect_input(user_input)

    def validate_output(self, output: str) -> dict:
        """
        Validate outgoing LLM response.
        """

        return self.middleware.inspect_output(output)

    def run(self, agent: Any, user_input: str) -> dict:
        """
        Secure execution wrapper.

        NOTE:
        This is framework-independent.

        Actual ADK execution will be
        connected during Phase 5.
        """

        input_result = self.validate_input(user_input)

        if not input_result["allowed"]:
            return input_result

        return {
            "allowed": True,
            "agent": getattr(agent, "name", "Unknown Agent"),
            "clean_input": input_result["clean_text"],
            "message":
                "Input validated successfully. "
                "Agent execution will be integrated in Phase 5."
        }