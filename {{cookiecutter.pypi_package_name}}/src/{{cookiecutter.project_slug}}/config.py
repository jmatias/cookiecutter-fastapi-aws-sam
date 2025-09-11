import os

from dotenv import load_dotenv

load_dotenv()

AWS_LAMBDA = os.getenv("AWS_LAMBDA_FUNCTION_NAME") is not None

FASTAPI_ROOT_PATH = "/Dev" if AWS_LAMBDA else ""

securiy_dependencies = []

cors_origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]


_local_environment = "Local environment"
swagger_servers = [
    {
        "url": "http://localhost:8000",
        "description": _local_environment,
    },
    {
        "url": "http://127.0.0.1:8000",
        "description": _local_environment,
    },
    {
        "url": "http://localhost:3000",
        "description": "Local SAM deployment",
    }
]
