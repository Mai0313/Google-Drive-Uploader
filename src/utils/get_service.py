"""This function is only for getting service and build service."""

from googleapiclient.discovery import build

from src.utils.get_creds import creds


def get_service():
    """Builds the service for Google Drive.

    Returns:
        service: service
    """
    service = build('drive', 'v3', credentials=creds)
    return service


service = get_service()
