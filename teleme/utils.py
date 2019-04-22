"""
Utilities.
"""
import json
import os
from typing import Optional
from pydantic import BaseModel

class SecretsBase(BaseModel):
    id: int = ...
    hash: str = ...

def get_secrets(path: Optional[str] = None) -> dict:
    """Loads secrets.
    
    Args:
    =====
        path (str): A filepath from which secrets will be downloaded from.
    """
    if path is None:
        filename = "secrets.json"
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", filename)
    
    with open(path, "r") as f:
        secrets = json.load(f)

    secrets = SecretsBase(**secrets)

    return secrets
    