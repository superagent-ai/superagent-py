# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .vector_db_provider import VectorDbProvider

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class PrismaModelsVectorDb(pydantic.BaseModel):
    """
    Represents a VectorDb record
    """

    id: str
    provider: VectorDbProvider
    options: typing.Optional[str]
    datasources: typing.Optional[typing.List[PrismaModelsDatasource]]
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt")
    api_user_id: str = pydantic.Field(alias="apiUserId")
    api_user: typing.Optional[PrismaModelsApiUser] = pydantic.Field(alias="apiUser")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}


from .prisma_models_api_user import PrismaModelsApiUser  # noqa: E402
from .prisma_models_datasource import PrismaModelsDatasource  # noqa: E402

PrismaModelsVectorDb.update_forward_refs()