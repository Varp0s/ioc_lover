import asyncio
from schemes.schemas import IoCType
from datetime import datetime
from logger import log
from models.model import IocModel, create_tables
from db.session import SessionLocal
from .scripts.ck_vt import check_analysis
from .scripts.ck_dns import check_dns_record
from .scripts.ck_malw import check_malicious
from .scripts.ck_who import check_whois
from .scripts.ck_censys import check_censys
from .scripts.ck_urlscan import check_urlscan
from .scripts.geo import check_geo_location
from typing import Any


async def analyze_ioc(ioc_value: str) -> dict[str, Any]:
    """
    Analyze the provided IOC value.

    Args:
        ioc_value: Value of the IOC.
    
    Returns:
        A dictionary containing IOC types and their corresponding values. 
    """
    await create_tables()

    results = await asyncio.gather(
        check_malicious(ioc_value),
        check_analysis(ioc_value),
        check_whois(ioc_value),
        fetch_dns_records(ioc_value),
        check_geo_location(ioc_value),
        check_censys(ioc_value),
        check_urlscan(ioc_value),
    )

    results = dict(zip(ioctype, results))

    log.info(f"Starting analysis: {ioc_value}")

    async with AsyncSessionLocal() as db:
        try:
            ioc_model_object = IoCModel(
                added_at=datetime.now(),
                malicious_control=str(results[ioctype.MALICIOUS_CONTROL]),
                vt=str(results[ioctype.VT]),
                whois=str(results[ioctype.WHOIS]),
                dns_record=str(results[ioctype.DNS_RECORD]),
                geometric_location=str(results[IoCType.GEO_LOCATION]),
                censys=str(results[ioctype.CENSYS]),
                urlscan=str(results[ioctype.URLSCAN]),
            )
            db.add(ioc_model_object)
            await db.commit()
        finally:
            await db.close()

    return results
