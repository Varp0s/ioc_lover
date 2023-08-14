from fastapi import APIRouter, Query, Request, HTTPException
from check.ioc_crawler import analyze_ioc


router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Server is running! site map /search usage: /search?ioc_value=<IOC_VALUE>"}

@router.get("/search")
async def search_ioc(ioc_value: str = Query(..., alias="ioc_value")):
    cleaned_ioc_value = ioc_value.strip()  

    results = await analyze_ioc(cleaned_ioc_value)

    return results

print(search_ioc)