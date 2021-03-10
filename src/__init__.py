from flask_restx import Api
from flask import Blueprint

from .main.controller.sowing_form_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='GAP-A-FARM WEB-SERVICE',
          version='1.0',
          description='restx web service'
          )

api.add_namespace(user_ns, path='/user')
