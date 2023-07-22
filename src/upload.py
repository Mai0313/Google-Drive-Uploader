"""This module is used to upload files and create folders on Google Drive.

Main functions:
    - upload_file: Uploads files to Google Drive.
        - Input must be a list of file paths.
    - create_folder: Creates folders on Google Drive.
        - Input must be a string of the folder name.
"""

import os
import mimetypes
from pydantic import BaseModel, Field
from tqdm import tqdm

from googleapiclient.http import MediaFileUpload
from src.utils.get_service import service


class UpdateFileCheck(BaseModel):
    """Data Type Check.

    Args:
        targets (list[str]): This is a function to check if the input is a list of strings.
        target_folder_id (str): list of string of the folder from Google Drive.
    """
    targets: list[str]
    target_folder_id: list[str]


class CreateFolderCheck(BaseModel):
    """Data Type Check.

    Args:
        foldername (list): This should be a path of a folder.
        target_folder_id (list[str]): list of string of the folder from Google Drive.
    """
    foldername: list
    target_folder_id: list[str]


def get_execution(file_metadata: dict, media=None):
    """_summary_.

    Args:
        file_metadata (dict): file_metadata
        media (_type_, optional): It will be determined automatically, but if you wanna create a folder, it needs to be given. Defaults to None.

    Returns:
        str: folder id or file id
    """
    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()
    return file.get('id')


def upload_file(targets: list, target_folder_id: str = None):
    """_summary_.

    Args:
        targets (list): A list of file paths you wanna upload to Google Drive.
        target_folder_id (str, optional): If this is given, it will upload the file right under.
    """
    UpdateFileCheck(targets=targets, target_folder_id=target_folder_id)
    for target in targets:
        print(f"Uploading {target} to Google Drive")
        file_metadata = {
            'name': os.path.basename(target),
            'mimeType': mimetypes.MimeTypes().guess_type(target)[0],
            'parents': target_folder_id,
        }
        media = MediaFileUpload(target)
        file = get_execution(file_metadata=file_metadata, media=media)


def create_folder(foldername: str, target_folder_id: str = None):
    """Create a folder on Google Drive.

    Args:
        foldername (str): The name you want to give to the folder.
        target_folder_id (str, optional): If this is given, it will create a folder under the selected folder. Defaults to None.

    Returns:
        file_id (dict): this is the folder id of the created folder
    """
    CreateFolderCheck(foldername=foldername, target_folder_id=target_folder_id)
    print(f"Creating the folder named {foldername} on Google Drive")
    file_metadata = {
        'name': foldername,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': target_folder_id,
    }
    file = get_execution(file_metadata=file_metadata)
    return file
