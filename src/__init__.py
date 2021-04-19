from flask_restx import Api
from flask import Blueprint

from .main.controller.sowing_form_controller import api as sowing_form_ns
from .main.controller.harvesting_form_controller import api as harvest_form_ns
from .main.controller.issue_form_controller import api as issue_form_ns
from .data.controller.issue_form_controller import api as issue_sql
from .main.controller.application_form_controller import api as application_form_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='GAP-A-FARM WEB-SERVICE',
          version='1.0',
          description='restx web service'
          )

api.add_namespace(sowing_form_ns, path='/sowing_form')
api.add_namespace(harvest_form_ns, path='/harvesting_form')
api.add_namespace(issue_form_ns, path='/issue_form')
api.add_namespace(issue_sql, path='/issue_sql')
api.add_namespace(application_form_ns, path='/application_form')
