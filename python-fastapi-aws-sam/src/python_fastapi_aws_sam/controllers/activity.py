from typing import List

from fastapi import APIRouter

from python_fastapi_aws_sam.model import Activity

router = APIRouter()


@router.get(
    path="",
    response_model=List[Activity],
    operation_id="list_activities",
)
def list_activities():
    return [
        Activity()
    ]
