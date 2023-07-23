import os
import mimetypes

from googleapiclient.http import MediaFileUpload
from src.utils.creditional_gen import service
from src.utils.input_validation import UpdateFileCheck, CreateFolderCheck


def get_execution(file_metadata: dict, media=None):
    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()
    return file.get('id')


def upload_file(targets: list, target_folder_id: str = None):
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
    CreateFolderCheck(foldername=foldername, target_folder_id=target_folder_id)
    print(f"Creating the folder named {foldername} on Google Drive")
    file_metadata = {
        'name': foldername,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': target_folder_id,
    }
    file = get_execution(file_metadata=file_metadata)
    return file
