import httpx
from typing import Dict, Any

async def fetch_urlscan_data(ioc_value: str) -> Dict[str, Any]:
    """
    Fetches URLScan data for the provided IOC value from the URLScan API.

    Args:
        ioc_value (str): The IOC value to fetch URLScan data for.
    
    Returns:
        dict: URLScan data retrieved from the URLScan API.
    
    Raises:
        httpx.HTTPStatusError: If the response status code is not 200.
        Exception: If an error occurs while fetching or decoding the data.
    """
    url = f"https://urlscan.io/api/v1/search/?q={ioc_value}"
    headers = {"Content-Type": "application/json"}
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

def analyze_urlscan_data(ioc_value: str) -> Dict[str, Any]:
    """
    Analyzes the provided IOC value using URLScan data.

    Args:
        ioc_value (str): The IOC value to analyze using URLScan data.
    
    Returns:
        dict: URLScan data analysis results.
    """
    return fetch_urlscan_data(ioc_value)

async def check_urlscan(ioc_value: str) -> Dict[str, Any]:
    """
    Checks the URLScan analysis for the provided IOC value.

    Args:
        ioc_value (str): The IOC value to check URLScan analysis for.
    
    Returns:
        dict: URLScan data analysis results.
    """
    return await analyze_urlscan_data(ioc_value)
