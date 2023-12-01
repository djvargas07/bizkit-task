import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


def create_response(message, start_time, status_code=200):
    return {"message": message, "elapsedTime": time.time() - start_time}, status_code

@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if is_match(*MATCHES[match_id]) else "No match"
    return create_response(msg)



def is_match(fave_numbers_1, fave_numbers_2):
    return set(fave_numbers_2).issubset(set(fave_numbers_1))
