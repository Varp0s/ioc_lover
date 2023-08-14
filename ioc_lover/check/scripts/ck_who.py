import httpx
import config
from logger import log


async def fetch_whois_data(ioc_value):
    url = f"https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={config.whois_api_key}&domainName={ioc_value}&outputFormat=json"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json() 

def analyze_whois_data(ioc_value):
    return fetch_whois_data(ioc_value)


async def check_whois(ioc_value):
    return await analyze_whois_data(ioc_value)
