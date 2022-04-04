import pandas as pd

_DATA = pd.read_csv("50_states.csv")


def get_states():
    return _DATA["state"].to_list()


def state_exists(state):
    return state in get_states()


def get_state_pos(state):
    state_row = _DATA[_DATA["state"] == state]
    return int(state_row["x"]), int(state_row["y"])


def get_missing_states(guessed_states):
    return [state for state in get_states() if state not in guessed_states]


def save_missing_states(guessed_states):
    new_data = pd.DataFrame(get_missing_states(guessed_states))
    new_data.to_csv("states_to_learn.csv")
