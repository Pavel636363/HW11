import json

def load_candidates_from_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_candidate(candidate_id):
    pass


def candidates_by_name(candidate_name):
    pass


def candidates_by_scill(scill_name):
    pass


