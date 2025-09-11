from typing import List

from fastapi import APIRouter

from {{cookiecutter.project_slug}}.model import Activity

router = APIRouter()


@router.get(
    path="",
    response_model=List[str],
    operation_id="list_vegetables",
)
def list_vegetables():
    return ["Carrot", "Broccoli", "Spinach"]
