from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/",
    tags=["Debugging"],
    operation_id="hello",
)
def hello_world():
    return {"message": "Hello, wossrld!"}
