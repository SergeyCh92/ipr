from pydantic import Field
from pydantic_settings import BaseSettings


class ServiceSettings(BaseSettings):
    gateway_service_url: str = Field(validation_alias="GATEWAY_SERVICE_URL")
    exchange: str = Field(validation_alias="EXCHANGE", default="gpn_exchange")
    ipr_queue: str = Field(validation_alias="IPR_QUEUE", default="ipr")
