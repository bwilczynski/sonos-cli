from sonos.config import local_store

ACTIVE_HOUSEHOLD_FILE = "household.json"


def save_active_household(household):
    local_store.save(ACTIVE_HOUSEHOLD_FILE, household)


def get_active_household():
    return local_store.load(ACTIVE_HOUSEHOLD_FILE)
