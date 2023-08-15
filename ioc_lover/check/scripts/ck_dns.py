import httpx
import config
from logger import log
from typing import Dict, Any

async def fetch_dns_records(ioc_value: str) -> Dict[str, Any]:
    """
    Fetches DNS records for the provided IOC value from the Geekflare API.

    Args:
        ioc_value (str): The IOC value (URL) to fetch DNS records for.
    
    Returns:
        dict: DNS records retrieved from the Geekflare API.
    
    Raises:
        Exception: If an error occurs while fetching or decoding the data.
    """
    url = "https://api.geekflare.com/dnsrecord"
    headers = {
        "x-api-key": config.geekflare_api_key,
        "Content-Type": "application/json",
    }
    data = {
        "url": ioc_value,
        "proxyCountry": "tr",
        "followRedirect": True,
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            response_data = response.json()
            return response_data
        else:
            log.error(f"Failed to fetch DNS records for {ioc_value}. Status code: {response.status_code}")
            raise Exception(f"Failed to fetch DNS records for {ioc_value}. Status code: {response.status_code}")

async def check_dns_record(ioc_value: str) -> Dict[str, Any]:
    """
    Checks the DNS records for the provided IOC value.

    Args:
        ioc_value (str): The IOC value to check DNS records for.
    
    Returns:
        dict: DNS records retrieved from the Geekflare API.
    
    Raises:
        Exception: If an error occurs while fetching or decoding the data.
    """
    return await fetch_dns_records(ioc_value)
