from flask import request
from flask_restx import Resource

from ..util.dto import IssueFormDto
from ..service.issue_form_service import complete_prediction

api = IssueFormDto.api
_issue_form = IssueFormDto.issue_form
_issue_form_field_based = IssueFormDto.issue_form_field_based


@api.route('/')
class SowingForm(Resource):
    @api.response(201, 'Prediction complete.')
    @api.doc('make sowing form prediction on all fields')
    @api.expect(_issue_form, validate=True)
    def post(self):
        """Predicts entire form based on form received"""
        data = request.json
        return complete_prediction()


@api.route('/field_based')
class SowingForm(Resource):
    @api.response(200, 'Prediction complete.')
    @api.doc('make sowing form prediction on specific fields')
    @api.expect(_issue_form_field_based, validate=True)
    def post(self):
        """Predicts specific fields based on form received"""
        data = request.jsons
        return null
