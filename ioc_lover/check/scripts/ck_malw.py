import httpx
import config
from logger import log
from typing import Optional, Dict, Any

async def fetch_malicious_info(ioc_value: str) -> Optional[Dict[str, Any]]:
    """
    Fetches malicious information for the provided IOC value from AlienVault OTX API.

    Args:
        ioc_value (str): The IOC value to fetch malicious information for.
    
    Returns:
        dict or None: Malicious information retrieved from the AlienVault OTX API.
                      Returns None if the information could not be fetched or decoded.
    """
    url = f'https://otx.alienvault.com/api/v1/indicators/domain/{ioc_value}'
    headers = {'X-OTX-API-KEY': config.alienvault}
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            try:
                data = response.json()
                return data
            except httpx.JSONDecodeError:
                log.error(f"Failed to decode JSON response for {ioc_value}")
                return None
        else:
            log.error(f"Failed to fetch malicious information for {ioc_value}. Status code: {response.status_code}")
            return None

def analyze_malicious_info(ioc_value: str) -> Optional[Dict[str, Any]]:
    """
    Analyzes the malicious information for the provided IOC value.

    Args:
        ioc_value (str): The IOC value to analyze malicious information for.
    
    Returns:
        dict or None: Malicious information analysis results.
                      Returns None if the information could not be fetched or decoded.
    """
    return fetch_malicious_info(ioc_value)

async def check_malicious(ioc_value: str) -> Optional[Dict[str, Any]]:
    """
    Checks the malicious information for the provided IOC value.

    Args:
        ioc_value (str): The IOC value to check malicious information for.
    
    Returns:
        dict or None: Malicious information analysis results.
                      Returns None if the information could not be fetched or decoded.
    """
    return await analyze_malicious_info(ioc_value)
