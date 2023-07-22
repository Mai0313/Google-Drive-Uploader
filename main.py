"""This module is used to upload files to Google Drive."""

import os

from src.upload import upload_file, create_folder

filenames = [
    os.path.abspath(os.path.join("demo", f)) for f in os.listdir("demo")
]

if __name__ == "__main__":
    upload_file(filenames, "1Ldp_44E2hiJn9g5e8G0v-IwlZDLT9V6y")
