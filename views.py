from flask import jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from marshmallow import ValidationError

from app import app, db
from models import TA
from schema import TACreateSchema,TAUpdateSchema
from view_utils import parse_ta_data

jwt = JWTManager(app)

ta_create_schema = TACreateSchema()

ta_update_schema = TAUpdateSchema()


@app.route('/token/', methods=['POST'])
def get_token():
    try:
        email = request.json['email']
        access_token = create_access_token(identity=email)
        return jsonify(message='Token generated successfully.',
                       access_token=access_token), 200
    except Exception as exception_message:
        return jsonify(message='error: {}. '.format(exception_message)), 500


@app.route('/apis/ta/<id>', methods=['GET'])
@jwt_required()
def get_ta(id):
    ta = TA.query.get(id)
    if not ta:
        return jsonify(message='Teaching Assistant data not found.'), 404
    return jsonify(data=parse_ta_data(ta_create_schema.dump(ta))), 200


@app.route('/apis/ta/', methods=['GET'])
@jwt_required()
def get_tas():
    tas = []
    for ta in db.session.query(TA).all():
        tas.append(parse_ta_data(ta_create_schema.dump(ta)))
    return jsonify(data=tas), 200


@app.route('/apis/ta/', methods=['POST'])
@jwt_required()
def create_ta():
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    try:
        data = ta_create_schema.load(json_data)
    except ValidationError as err:
        return jsonify(message=err.messages), 400

    parsed_ta_data = parse_ta_data(data)
    ta = TA(**parsed_ta_data)

    try:
        db.session.add(ta)
        db.session.commit()
        return jsonify(message='Teaching Assistant data successfully created.',
                       ta_id=ta.id), 200
    except Exception as exception_message:
        return jsonify(message='error: {}. '.format(exception_message)), 500


@app.route('/apis/ta/<id>', methods=['PUT'])
@jwt_required()
def update_ta(id):
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    try:
        data = ta_update_schema.load(json_data)
    except ValidationError as err:
        return jsonify(message=err.messages), 400

    parsed_ta_data = parse_ta_data(data)

    try:
        db.session.query(TA).filter_by(id=id).update(parsed_ta_data)
        db.session.commit()
        return jsonify(message='Teaching Assistant data updated.'), 200
    except Exception as exception_message:
        return jsonify(message='error: {}. '.format(exception_message)), 500


@app.route('/apis/ta/<id>', methods=['DELETE'])
@jwt_required()
def delete_ta(id):
    db.session.query(TA).filter_by(id=id).delete()
    db.session.commit()
    return jsonify(message='Teaching Assistant data deleted.'), 200
