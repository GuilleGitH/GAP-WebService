from flask_restx import Namespace, fields


class SowingFormDto:
    api = Namespace(
        'sowing_form', description='sowing_form related operations')
    sowing_form = api.model('sowing_form', {
        'date': fields.Date(required=True, description='partial form'),
        'time': fields.DateTime(required=True, description='partial form'),
        'plot': fields.Integer(required=True, description='partial form'),
        'crop': fields.String(required=True, description='partial form'),
        'quantity': fields.Integer(required=True, description='partial form'),
        'time_to_harvest': fields.String(required=True, description='partial form'),
        'harvest_duration': fields.String(required=True, description='partial form'),
        'expected_yield': fields.String(required=True, description='partial form'),
        'note': fields.String(required=True, description='partial form'),
    })

    sowing_form_field_based = api.model('sowing_form_field_based', {
        'sowing_form': fields.Nested(sowing_form, required=True),
        'fields_required': fields.List(fields.Integer, default=None, required=True, description="fields to make predictions on"), })


class HarvestingFormDto:
    api = Namespace('harvesting_form',
                    description='harvesting_form related operations')
    harvesting_form = api.model('harvesting_form', {
        'date': fields.Date(required=True, description='partial form'),
        'time': fields.DateTime(required=True, description='partial form'),
        'plot': fields.Integer(required=True, description='partial form'),
        'quantity': fields.Integer(required=True, description='partial form'),
        'harvest_quantity': fields.String(required=True, description='partial form'),
        'note': fields.String(required=True, description='partial form'),
    })

    harvesting_form_field_based = api.model('harvesting_form_field_based', {
        'harvesting_form': fields.Nested(harvesting_form, required=True),
        'fields_required': fields.List(fields.Integer, default=None, required=True, description="fields to make predictions on"), })


class IssueFormDto:
    api = Namespace('issue_form',
                    description='issue_form related operations')
    issue_form = api.model('issue_form', {
        'date': fields.Date(required=True, description='partial form'),
        'time': fields.DateTime(required=True, description='partial form'),
        'plot': fields.Integer(required=True, description='partial form'),
        'issue_type': fields.Integer(required=True, description='partial form'),
        'description': fields.String(required=True, description='partial form'),
        'note': fields.String(required=True, description='partial form'),
    })

    issue_form_field_based = api.model('issue_form_field_based', {
        'issue_form': fields.Nested(issue_form, required=True),
        'fields_required': fields.List(fields.Integer, default=None, required=True, description="fields to make predictions on"), })


class ApplicationFormDto:
    api = Namespace('application_form',
                    description='application_form related operations')

    application_form = api.model('application_form', {
        'date': fields.Date(required=True, description='partial form'),
        'time': fields.DateTime(required=True, description='partial form'),
        'plot': fields.Integer(required=True, description='partial form'),
        'product': fields.String(required=True, description='partial form'),
        'quantity': fields.Integer(required=True, description='partial form'),
        'dose': fields.Float(required=True, description='partial form'),
        'machine': fields.String(required=True, description='partial form'),
        'note': fields.String(required=True, description='partial form'),
    })

    application_form_field_based = api.model('application_form_field_based', {
        'application_form': fields.Nested(application_form, required=True),
        'fields_required': fields.List(fields.Integer, default=None, required=True, description="fields to make predictions on"), })
