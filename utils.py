import json

from config import json_path


def load_data():
    """
    Загружает файл кандидатов
    :return: data
    """

    info = json_path
    with open(info, "r", encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_candidates():
    """
    Список кандидатов
    :return:
    """
    data = load_data()
    return data


def get_candidates_by_pk(pk):
    """
    Получает кандидата по РК
    :param pk:
    :return:candidate
    """
    candidates = load_data()
    for c in candidates:
        if c["id"] == pk:
            return c


def get_candidates_by_skill(skill):
    """
    Получает кандидата по скилу
    :param skill:
    :return:candidates list
    """

    skilled_candidates = []
    candidates = load_data()

    for c in candidates:
        skills = c["skills"].lower().strip().split(", ")
        if skill in skills:
            skilled_candidates.append(c)
    return skilled_candidates
