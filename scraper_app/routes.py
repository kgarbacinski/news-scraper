from flask import Blueprint, jsonify

from api.scraper import ContentGetter

endpoint_blueprint = Blueprint("endpoint", __name__)


@endpoint_blueprint.route("/get/<keyword>", methods=["GET"])
def endpoint(keyword):
    getter = ContentGetter(keyword)
    result = getter.get()
    
    if all(len(value) == 0 for value in result.values()):
        return jsonify('No keyword found!')
    else: 
        return jsonify(result) 