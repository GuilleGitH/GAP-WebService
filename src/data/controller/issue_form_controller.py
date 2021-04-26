from flask import request
from flask_restx import Resource

from ..util.dto import IssueFormDto, IssueDto
from ..service.issue_form_service import save_new_issue, get_all_issues

api = IssueFormDto.api
_issue = IssueDto.issue
_issue_form = IssueFormDto.issue_form
_issue_form_field_based = IssueFormDto.issue_form_field_based


@api.route('/')
class IssueForm(Resource):
    @api.response(201, 'Prediction complete.')
    @api.doc('make sowing form prediction on all fields')
    @api.expect(_issue_form, validate=True)
    def post(self):
        """Predicts entire form based on form received"""
        data = request.json
        return save_new_issue("asd")

    @api.marshal_list_with(_issue, envelope='data')
    def get(self):
        return get_all_issues()
