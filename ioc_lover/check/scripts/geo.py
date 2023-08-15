import httpx
import config
from logger import log
from typing import Optional

async def check_geo_location(ioc_value: str) -> Optional[str]:
    """
    Fetches geographical location information for the provided IP address.

    Args:
        ioc_value (str): The IP address to fetch geographical information for.
    
    Returns:
        str: A string containing the country name, region name, and city of the IP address.
             Returns None if the location information could not be fetched.
    """
    url = f"http://api.ipstack.com/{ioc_value}"
    params = {
        "access_key": config.IPSTACK_API_KEY
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)

        if response.status_code == 200:
            result = response.json()
            return f"{result['country_name']}, {result['region_name']}, {result['city']}"
        else:
            log.error(f"Failed to fetch GEO location for {ioc_value}. Status code: {response.status_code}")
            return None
