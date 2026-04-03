import os

from dotenv import load_dotenv

load_dotenv()

AWS_LAMBDA = os.getenv("AWS_LAMBDA") == "true" or os.getenv("AWS_LAMBDA_FUNCTION_NAME") is not None
API_GATEWAY_STAGE = os.getenv("API_GATEWAY_STAGE", "Dev")
LOCALSTACK = os.getenv("LOCALSTACK") == "true"

FASTAPI_ROOT_PATH = f"/{API_GATEWAY_STAGE}" if AWS_LAMBDA else ""

security_dependencies = []

# For local development, allow all origins. In production, restrict this.
cors_origins = ["*"] if AWS_LAMBDA else [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]


_local_environment = "Local environment"
swagger_servers = []

# Note: For LocalStack/AWS, the Swagger UI will dynamically discover the API Gateway URL
# from the request context. We'll add it dynamically in the FastAPI app if needed.
# For now, use wildcard CORS to allow any origin when deployed.

# Add local development servers
if not AWS_LAMBDA:
    swagger_servers.extend([
        {
            "url": "http://localhost:8000",
            "description": _local_environment,
        },
        {
            "url": "http://127.0.0.1:8000",
            "description": _local_environment,
        },
    ])
