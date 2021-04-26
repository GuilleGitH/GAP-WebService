from flask import request
from flask_restx import Resource

from ..util.dto import SowingFormDto
from ..service.sow_form_service import save_new_sow, get_all_sow

api = SowingFormDto.api
_sow_form = SowingFormDto.sowing_form


@api.route('/')
class SowingForm(Resource):
    @api.response(201, 'Prediction complete.')
    @api.doc('make sowing form prediction on all fields')
    @api.expect(_sow_form, validate=True)
    def post(self):
        """Predicts entire form based on form received"""
        data = request.json
        return save_new_sow(data)

    @api.marshal_list_with(_sow_form, envelope='data')
    def get(self):
        return get_all_sow()
