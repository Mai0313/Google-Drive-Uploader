"""This module is used to create credentials for Google Drive.

Main functions:
    - get_creditials: Creates credentials for Google Drive.
"""

import os

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


def get_creditials():
    """Creates credentials for Google Drive.

    Returns:
        creds: creds from Google Drive, which is a dict
    """
    SCOPES = ['https://www.googleapis.com/auth/drive']
    creds = None
    if os.path.exists('config/token.json'):
        creds = Credentials.from_authorized_user_file('config/token.json',
                                                      SCOPES)  # noqa

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'config/credentials.json', SCOPES)  # noqa
        creds = flow.run_local_server(port=0)
        with open('config/token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


creds = get_creditials()
