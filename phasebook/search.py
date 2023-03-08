from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    result = []

    if len(request.args) == 0:
        return USERS

    id = request.args.get("id")
    name = request.args.get("name")
    age = request.args.get("age")
    occupation = request.args.get("occupation")

    for i in range(len(USERS)):
        if id is not None and id == USERS[i]["id"]:
            result.append(USERS[i])
            continue

        if name is not None:
            wholename = (USERS[i]["name"]).split()
            if name == wholename[0] or name == wholename[1]:
                result.append(USERS[i])
                continue

        if age is not None:
            age = int(age)
            age_max = age + 1
            min_age = age - 1
            if age == USERS[i]["age"] or age_max == USERS[i]["age"] or min_age == USERS[i]["age"]:
                result.append(USERS[i])
                continue

        if occupation is not None:
            partial = len(occupation)
            real_occupation = USERS[i]["occupation"]
            if occupation == USERS[i]["occupation"] or occupation[:partial] == real_occupation[:partial]:
                result.append(USERS[i])
                continue

    return result
