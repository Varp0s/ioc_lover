import httpx

async def fetch_urlscan_data(ioc_value):

    url = f"https://urlscan.io/api/v1/search/?q={ioc_value}"

    headers = {
        "Content-Type": "application/json",
    }
    

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

def analyze_urlscan_data(ioc_value):
    return fetch_urlscan_data(ioc_value)

async def check_urlscan(ioc_value):
    return await analyze_urlscan_data(ioc_value)
