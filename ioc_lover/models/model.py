from schemes.schemas import IoCType
from sqlalchemy import MetaData, Table, Column, Integer, JSON, DateTime
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base
from db.session import engine

import enum

Base = declarative_base()

class IocType(enum.Enum):
    """
    Enumeration class representing different types of IoCs (Indicators of Compromise).
    """
    MALICIOUS_CONTROL = "malicious_control"  
    VT = "vt"                    
    WHOIS = "whois"                        
    DNS_RECORD = "dns_record"      
    GEO_LOCATION = "geometric_location"         
    CENSYS = "censys"                       
    URLSCAN = "urlscan"      


class IocModel(Base):
    """
    Database model for IoC data.

    Args:
        Base: Database base.
    """
    __tablename__ = 'ioc_analysis'

    id = Column(Integer, primary_key=True, index=True)
    added_at = Column(DateTime)
    malicious_control = Column(JSON)
    analysis = Column(JSON)
    whois = Column(JSON)
    geometric_location = Column(JSON)
    dns_record = Column(JSON)
    censys = Column(JSON)
    urlscan = Column(JSON)

async def create_tables():
    """
    Create database tables.

    Args:
        Base: Database base.
    """
    conn = await engine.begin()
    try:
        await conn.run_sync(Base.metadata.create_all)
    finally:
        await conn.close()
