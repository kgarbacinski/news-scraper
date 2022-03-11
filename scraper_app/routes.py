from flask import Blueprint, jsonify

from api.scraper import ContentGetter

endpoint_blueprint = Blueprint("endpoint", __name__)


@endpoint_blueprint.route("/get/<keyword>", methods=["GET"])
def endpoint(keyword):
    getter = ContentGetter(keyword)
    result = getter.get()
    
    if all(not len(value) for value in result.values()):
        return jsonify(f'No content with keyword: {keyword}')
    else: 
        return jsonify(result) 