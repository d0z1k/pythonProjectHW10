def html_candidate(candidate):
    """
    Возвращает  данные по указанному кандидату с картинкой
    :param candidate: int
    :return: candidate_code
    """

    candidate_code = ""

    candidate_code += f"<img src=\"{candidate['picture']}\">\n"
    candidate_code += f"{candidate['name']}\n"
    candidate_code += f"{candidate['skills']}\n"
    candidate_code += f"{candidate['position']}\n"
    return "<pre>" + candidate_code + "<pre>"


def html_candidates(candidates):
    """
    Возвращает данные по кандидатам с указанным скилом
    :param candidates: skill
    :return: candidates_code
    """

    candidates_code = ""

    for c in candidates:
        candidates_code += f"{c['name']}\n"
        candidates_code += f"{c['skills']}\n"
        candidates_code += f"{c['position']}\n"

    return "<pre>" + candidates_code + "<pre>"
