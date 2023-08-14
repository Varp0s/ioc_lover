import uvicorn
from logger import log
from api.v1.api import api_router
import config

if __name__ == "__main__":
    log.info("Starting the API server...")
    uvicorn.run(api_router, host=config.sv_host, port=config.sv_port)
