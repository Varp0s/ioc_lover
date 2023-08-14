import httpx
import config
from logger import log

censys_client = httpx.AsyncClient()

async def fetch_censys_data(ioc_value):
    url = f"https://search.censys.io/api/v2/certificates/search?q={ioc_value}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Basic {config.censys_api}"
    }

    response = await censys_client.get(url, headers=headers)
    return response

def analyze_censys_data(response):
    if response.status_code == 200:
        return response.text
    else:

        log.error(f"Failed to fetch Censys data. Status code: {response.status_code}")
        return None


async def check_censys(ioc_value):
    response = await fetch_censys_data(ioc_value)
    return analyze_censys_data(response)
