# Google Drive Updater

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Mai0313/Google-Drive-Uploader/master.svg)](https://results.pre-commit.ci/latest/github/Mai0313/Google-Drive-Uploader/master)

### This is a simple program that can help you upload your file to Google Drive

#### In the pass, uploading files to Google Drive was a little bit annoying, so I made this program to help me upload my file to Google Drive.

#### The point is making it easier to upload files to Google Drive.

## The Main Feature

- `upload_file`: Upload your file to Google Drive, EXCEPT `folder`
  - `target`: This is a list you wanna upload
  - `target_folder_id`: This is the target folder you wanna save on Google Drive
    ```python
    upload_file(target, target_folder_id)
    ```
- `create_folder`: Create a folder and it will return a file id
  - `foldername`: This is a list you wanna upload
  - `target_folder_id`: This is the target folder you wanna save on Google Drive
    ```python
    create_folder(foldername, target_folder_id)
    ```

## How to get credentials

1. Enable Google Drive API
2. Create your own Ouath file called `client_secret.json`
3. Rename `client_secret.json` to `credentials.json`

### Once you run this program, you will see a panel tells you to login

### Just do whatever it tells you to do.

## For more Details, Please Check:

[How to Enable Google Drive API](https://support.google.com/googleapi/answer/6158841?hl=en "link")

[How to Get Your Client Secret](https://support.google.com/cloud/answer/6158849?hl=en "link")
