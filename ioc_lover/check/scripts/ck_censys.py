import httpx
import config
from logger import log
from typing import Optional

censys_client = httpx.AsyncClient()

async def fetch_censys_data(ioc_value: str) -> httpx.Response:
    """
    Fetches Censys data for the provided IOC value from the Censys API.

    Args:
        ioc_value (str): The IOC value to fetch Censys data for.
    
    Returns:
        httpx.Response: Response object from the Censys API.
    """
    url = f"https://search.censys.io/api/v2/certificates/search?q={ioc_value}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Basic {config.censys_api}"
    }

    response = await censys_client.get(url, headers=headers)
    return response

def analyze_censys_data(response: httpx.Response) -> Optional[str]:
    """
    Analyzes the Censys data response.

    Args:
        response (httpx.Response): Response object from the Censys API.
    
    Returns:
        str or None: Analyzed Censys data as text or None if an error occurred.
    """
    if response.status_code == 200:
        return response.text
    else:
        log.error(f"Failed to fetch Censys data. Status code: {response.status_code}")
        return None

async def check_censys(ioc_value: str) -> Optional[str]:
    """
    Checks the Censys data for the provided IOC value.

    Args:
        ioc_value (str): The IOC value to check Censys data for.
    
    Returns:
        str or None: Analyzed Censys data as text or None if an error occurred.
    """
    response = await fetch_censys_data(ioc_value)
    return analyze_censys_data(response)
