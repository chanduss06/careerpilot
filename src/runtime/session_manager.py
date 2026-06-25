from uuid import uuid4

from .execution_context import ExecutionContext


class SessionManager:
    """
    Creates and tracks runtime sessions.

    Phase 5.1:
    Only session creation.

    Phase 5.2:
    Memory integration.

    Phase 5.3:
    Persistent conversations.
    """

    def create_session(
        self,
        user_id: str = "default"
    ) -> ExecutionContext:

        return ExecutionContext(
            session_id=str(uuid4()),
            user_id=user_id
        )