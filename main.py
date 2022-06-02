from flask import Flask

import functions
import utils

app = Flask(__name__)


@app.route("/")
def page_candidates():
    """
    маршрут на страницу с кандидатами
    :return: page_candidates
    """
    candidates = utils.get_candidates()
    html_function = functions.html_candidates(candidates)
    return html_function


@app.route("/candidates/<int:pk>")
def page_candidate_pk(pk):
    """
    маршрут на страницу с определённыйм кандидатом
    :param pk: int
    :return: page_candidate_pk
    """
    candidate = utils.get_candidates_by_pk(pk)
    html_function = functions.html_candidate(candidate)
    return html_function


@app.route("/skills/<skill>")
def page_candidates_skill(skill):
    """
    маршрут на кандидата с указанным скилом
    :param skill: skill
    :return: page_candidates_skill
    """
    candidates = utils.get_candidates_by_skill(skill)
    html_function = functions.html_candidates(candidates)
    return html_function


app.run()
