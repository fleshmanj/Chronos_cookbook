import requests
import ast
import time


class APIHandler:

    def __init__(self, auth: tuple):
        self.auth = auth
        self.request_type = {"grant_type":"client_credentials"}
        self.access_token = None
        self.access_token_life = int

    def get_access_token(self):
        try:
            response = requests.request("POST", url="https://oauth.battle.net/token", data=self.request_type, auth=self.auth)
            decoded_response = ast.literal_eval(response.content.decode())
            self.access_token = decoded_response["access_token"]
            self.access_token_life = time.time() + decoded_response["expires_in"]
        except:
            print("Failed to get access token")

    def validate_token(self):
        if self.access_token == None:
            self.get_access_token()
        if self.access_token_life != None and float(self.access_token_life) > time.time():
            return
        else:
            self.get_access_token()
