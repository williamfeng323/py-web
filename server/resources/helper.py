from server.app import app
from flask import request
import json


@app.login_manager.unauthorized_handler
def unauth_handler():
    # reserve for further usage
    # if request.is_xhr:
    #     return json.dump({
    #         'success': False,
    #         'data': {'login_required': True},
    #         'message': 'Authorize please to access this page.'
    #     }, indent=2), 401
    # else:
    #     return 401
    return {
            'success': False,
            'data': {'login_required': True},
            'message': 'Authorize please to access this page.'
        }, 401
