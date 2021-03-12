from flask import request
from flask_restx import Resource

from ..util.dto import ApplicationFormDto
from ..service.application_form_service import complete_prediction

api = ApplicationFormDto.api
_application_form = ApplicationFormDto.application_form
_application_form_field_based = ApplicationFormDto.application_form_field_based


@api.route('/')
class ApplicationForm(Resource):
    @api.response(200, 'Prediction complete.')
    @api.doc('make sowing form prediction on all fields')
    @api.expect(_application_form, validate=True)
    def post(self):
        """Predicts entire form based on form received"""
        data = request.json
        return complete_prediction("all")


@api.route('/field_based')
class ApplicationForm(Resource):
    @api.response(200, 'Prediction complete.')
    @api.doc('make sowing form prediction on specific fields')
    @api.expect(_application_form_field_based, validate=True)
    def post(self):
        """Predicts specific fields based on form received"""
        data = request.json
        return complete_prediction(data['field_required'])
