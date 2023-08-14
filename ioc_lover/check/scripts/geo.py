import httpx
import config
from logger import log

async def check_geo_location(ioc_value):
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
            logger.error(f"Failed to fetch GEO location for {ioc_value}. Status code: {response.status_code}")
