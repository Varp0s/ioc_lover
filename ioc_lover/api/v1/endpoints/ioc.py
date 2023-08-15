from fastapi import APIRouter, Query
from typing import Any, Dict

from check.ioc_crawler import analyze_ioc

router = APIRouter()

@router.get("/")
async def root() -> Dict[str, str]:
    """
    Default route that returns a message indicating that the server is running.
    
    Returns:
        dict: A dictionary containing a message indicating that the server is running.
    """
    return {"message": "Server is running! To use, visit /search and provide an IOC value."}

@router.get("/search")
async def search_ioc(ioc_value: str = Query(..., alias="ioc_value")) -> Dict[str, Any]:
    """
    Searches for information about the provided IOC value.
    
    Args:
        ioc_value (str): The IOC value to search for.
    
    Returns:
        dict: A dictionary containing the analysis results for the provided IOC value.
    """
    cleaned_ioc_value = ioc_value.strip()  

    results = await analyze_ioc(cleaned_ioc_value)

    return results
