from fastapi import APIRouter

router = APIRouter()


@router.get(
    path="",
    response_model=list[str],
    operation_id="list_fruits",
)
def list_fruits():
    return ["Apple", "Banana", "Orange"]
