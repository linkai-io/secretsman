import os
import sys
import json
import falcon
import secretsman

APP_ENV = os.getenv('APP_ENV', None)
APP_REGION = os.getenv('APP_REGION', None)

class SecretsResource:
    def __init__(self):
        self.secrets = secretsman.Secrets(APP_ENV, APP_REGION)

    def on_get(self, req, resp):
        if self.secrets.GetPassword() == None:
            resp.status = falcon.HTTP_500
            resp.body = json.dumps({'error': 'empty password'})
            return

        resp.status = falcon.HTTP_200
        secret = self.secrets.GetPassword()
        resp.body = json.dumps({'secret': secret})

api = falcon.API()
api.add_route('/', SecretsResource())


    

