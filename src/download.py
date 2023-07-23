from googleapiclient.http import MediaIoBaseDownload
from src.utils.creditional_gen import service
import io

def download_file(file_id: str, destination: str):
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(destination, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
