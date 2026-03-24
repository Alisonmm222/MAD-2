import json
from pathlib import Path

def get_agent_with_opening_statement(directory):
    file_lookup = {f.name: f for f in directory.rglob("*.json")}
    def inner(path):
        full_path = file_lookup[Path(path).name]
        with open(full_path) as fp:
            data = json.load(fp)

        opening_agent = data["opening_statements"][0]["agent"].split("_")[0]  # "pro" or "con"

        return opening_agent
    return inner


def get_agent_who_starts(directory):
    file_lookup = {f.name: f for f in directory.rglob("*.json")}
    def inner(path):
        full_path = file_lookup[Path(path).name]
        with open(full_path, 'r') as fp:
            data = json.load(fp)

        nrounds = data["nrounds"]
        starting_agent = data["discussion_history"][f"Round_{nrounds}"][0]["agent"].split("_")[0]  # "pro" or "con"

        return starting_agent
    return inner