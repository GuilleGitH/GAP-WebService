from flask import request
from flask_restx import Resource

from ..util.dto import HarvestingFormDto

api = HarvestingFormDto.api
_harvesting_form = HarvestingFormDto.harvesting_form
_harvesting_form_field_based = HarvestingFormDto.harvesting_form_field_based


@api.route('/')
class HarvestingForm(Resource):
    @api.response(201, 'Prediction complete.')
    @api.doc('make harvest form prediction on all fields')
    @api.expect(_harvesting_form, validate=True)
    def post(self):
        """Predicts entire form based on form received"""
        data = request.json
        return null


@api.route('/field_based')
class HarvestingForm(Resource):
    @api.response(200, 'Prediction complete.')
    @api.doc('make sowing form prediction on specific fields')
    @api.expect(_harvesting_form_field_based, validate=True)
    def post(self):
        """Predicts specific fields based on form received"""
        data = request.jsons
        return null
