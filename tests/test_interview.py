from src.memory.interview_store import (
    save_interview_score,
    get_interview_scores
)

save_interview_score(75)

save_interview_score(82)

print(
    get_interview_scores()
)