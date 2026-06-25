from typing import Optional

from careerpilot_agent.agent import root_agent

from .response import RuntimeResponse
from .session_manager import SessionManager


class CareerPilotRunner:
    """
    Entry point for executing CareerPilot.

    Phase 5.3

    Responsibilities:

    • Create runtime session
    • Execute the root ADK orchestrator
    • Return runtime metadata

    Future phases will add:

    • Security middleware
    • Memory integration
    • MCP execution
    • Evaluation pipeline
    """

    def __init__(self):

        self.session_manager = SessionManager()
        self.root_agent = root_agent

    def start(
        self,
        user_id: str = "default"
    ) -> RuntimeResponse:

        session = self.session_manager.create_session(
            user_id=user_id
        )

        return RuntimeResponse(
            success=True,
            message="CareerPilot runtime initialized.",
            data={
                "session_id": session.session_id,
                "user_id": session.user_id,
                "root_agent": self.root_agent.name,
            },
        )

    def get_root_agent(self):
        """
        Returns the ADK root agent.

        Future execution layers will invoke this
        agent through ADK sessions.
        """

        return self.root_agent