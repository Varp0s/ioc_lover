from enum import Enum

from pydantic import BaseModel, field_validator

class IoCType(str, Enum):
    MALICIOUS_CONTROL = "malicious_control"
    GEO_LOCATION = "geometric_location"
    ANALYSIS = "analysis"
    WHOIS = "whois"
    DNS_RECORD = "dns_record"
    CENSYS = "censys"
    URLSCAN = "urlscan"

class IoCValue(BaseModel):
    ioc_value: str 
    
    @field_validator('ioc_value')
    def is_string(cls, v: str) -> str:
        if not isinstance(v, str):
            raise ValueError(f"{v} must be string")
        return v