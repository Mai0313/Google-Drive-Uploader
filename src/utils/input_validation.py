from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional, Any, Union


class UpdateFileCheck(BaseModel):
    targets: list[str]
    target_folder_id: Optional[list[str]]


class CreateFolderCheck(BaseModel):
    foldername: str
    target_folder_id: Optional[list[str]]
