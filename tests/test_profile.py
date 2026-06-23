from src.memory.profile_store import (
    save_profile,
    get_profile
)

save_profile(
    "Chandra",
    "Backend Developer"
)

print(get_profile())