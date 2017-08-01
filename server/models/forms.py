from flask_wtf import Form

from wtforms_alchemy import model_form_factory
from wtforms import StringField
from wtforms.validators import DataRequired

# from .server import db
from server.models.user import User

BaseModelForm = model_form_factory(Form)


class UserCreateForm(BaseModelForm):
    class Meta:
        model = User