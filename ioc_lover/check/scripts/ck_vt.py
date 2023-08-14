import httpx
import config
from logger import log

async def fetch_analysis_data(ioc_value):

    url = f"https://www.virustotal.com/api/v3/domains/{ioc_value}"
    

    headers = {"x-apikey": config.virustotal_api_key}
    
    async with httpx.AsyncClient() as virustotal_client:
        try:

            response = await virustotal_client.get(url, headers=headers)
            response.raise_for_status() 
            return response.json()  
        except httpx.HTTPStatusError as e:

            logger.error(f"Failed to fetch VirusTotal analysis data for {ioc_value}. Status code: {e.response.status_code}")
            raise Exception(f"Failed to fetch VirusTotal analysis data for {ioc_value}. Status code: {e.response.status_code}")
        except httpx.RequestError as e:
     
            logger.error(f"Request error while fetching VirusTotal analysis data for {ioc_value}: {str(e)}")
            raise Exception(f"Request error while fetching VirusTotal analysis data for {ioc_value}: {str(e)}")
        except httpx.JSONDecodeError:

            logger.error(f"Failed to decode JSON response for {ioc_value}.")
            raise Exception(f"Failed to decode JSON response for {ioc_value}.")


def analyze_ioc(ioc_value):

    analysis_data = fetch_analysis_data(ioc_value)
    analysis_results = analysis_data["data"]["attributes"]["last_analysis_results"]
    
    harmless_count = sum(1 for result in analysis_results.values() if result["category"] == "harmless")
    harmful_count = sum(1 for result in analysis_results.values() if result["category"] == "harmful")
    

    result_data = {
        "harmless_count": harmless_count,
        "harmful_count": harmful_count
    }
    return result_data


async def check_analysis(ioc_value):
    return await analyze_ioc(ioc_value)
