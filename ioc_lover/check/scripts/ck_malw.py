import httpx
import config
from logger import log


async def fetch_malicious_info(ioc_value):

    url = f'https://otx.alienvault.com/api/v1/indicators/domain/{ioc_value}'
    

    headers = {'X-OTX-API-KEY': config.alienvault}
    

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            try:
                data = response.json()
                return data
            except httpx.JSONDecodeError:
                logger.error(f"Failed to decode JSON response for {ioc_value}")
                return None
        else:
            logger.error(f"Failed to fetch malicious information for {ioc_value}. Status code: {response.status_code}")
            return None

def analyze_malicious_info(ioc_value):
    return fetch_malicious_info(ioc_value)


async def check_malicious(ioc_value):
    return await analyze_malicious_info(ioc_value)
