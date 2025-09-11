import json
from datetime import datetime, UTC
from enum import StrEnum

from faker import Faker
from pydantic import BaseModel, Field, typing
from starlette.responses import Response

fake = Faker()


class PrettyJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4,
            separators=(", ", ": "),
        ).encode("utf-8")


class Activity(BaseModel):
    # pass
    activity: str = Field(default_factory=lambda: fake.word())
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: str = Field(default_factory=lambda: datetime.now(UTC).isoformat())

    model_config = {
        "json_schema_extra": {
            "example": {
                "activity": "Running",
                "created_at": "2024-04-10T10:00:00Z",
                "updated_at": "2024-04-10T12:00:00Z",
            }
        }
    }



class AWSRegion(StrEnum):
    US_EAST_1 = "us-east-1"
    US_EAST_2 = "us-east-2"
    US_WEST_1 = "us-west-1"
    US_WEST_2 = "us-west-2"
