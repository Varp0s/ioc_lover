import httpx
import config
from logger import log


async def fetch_dns_records(ioc_value):

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


async def check_dns_record(ioc_value):
    response_data = await fetch_dns_records(ioc_value)
    return response_data
