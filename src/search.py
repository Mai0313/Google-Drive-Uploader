from src.utils.creditional_gen import service


def search_folder(
    target_folder_name: str
) -> list:  # This is only for searching folders; it is faster
    files = []
    page_token = None
    while True:
        response = service.files().list(
            q="mimeType='application/vnd.google-apps.folder'",
            spaces='drive',
            fields='nextPageToken, files(id, name)',
            pageToken=page_token).execute()
        for file in response.get('files', []):
            print(F'Found file: {file.get("name")}, {file.get("id")}')
            if file.get("name") == target_folder_name:
                files.append(file)
                return files  # Return immediately after finding the matching file
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
    return []  # Return an empty list if no matching file was found


def search_files(
    target_file_name: str
) -> list:  # This can search ALL files or folder; it might be slow
    files = []
    page_token = None
    while True:
        response = service.files().list(q=f"name='{target_file_name}'",
                                        spaces='drive',
                                        fields='nextPageToken, files(id, name)',
                                        pageToken=page_token).execute()
        for file in response.get('files', []):
            print(f'Found file: {file.get("name")}, {file.get("id")}')
            if file.get("name") == target_file_name:
                files.append(file)
                return files  # Return immediately after finding the matching file
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
    return []  # Return an empty list if no matching file was found
