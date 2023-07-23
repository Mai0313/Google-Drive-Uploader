"""This module is used to create credentials for Google Drive.

Main functions:
    - get_creditials: Creates credentials for Google Drive.
"""

import os

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


class CreditionalsGenerator:

    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/drive']
        self.creds = None

    def get_creditials(self):
        if os.path.exists('config/token.json'):
            self.creds = Credentials.from_authorized_user_file(
                'config/token.json', self.SCOPES)

        if not self.creds or not self.creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(
                'config/credentials.json', self.SCOPES)
            self.creds = flow.run_local_server(port=0)
            with open('config/token.json', 'w') as token:
                token.write(self.creds.to_json())
        return self.creds

    def get_service(self):
        creds = self.get_creditials()
        return build('drive', 'v3', credentials=creds)


service = CreditionalsGenerator().get_service()
