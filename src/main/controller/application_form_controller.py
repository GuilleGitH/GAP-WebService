from flask import request
from flask_restx import Resource

from ..util.dto import ApplicationFormDto
from ..service.sowing_form_service import save_new_user, get_all_users, get_a_user

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
        return null


@api.route('/field_based')
class ApplicationForm(Resource):
    @api.response(200, 'Prediction complete.')
    @api.doc('make sowing form prediction on specific fields')
    @api.expect(_application_form_field_based, validate=True)
    def post(self):
        """Predicts specific fields based on form received"""
        data = request.jsons
        return null
