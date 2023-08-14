import os
from dynaconf import Dynaconf
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

settings = Dynaconf(
    load_dotenv=True,
    dotenv_path=ROOT_DIR.joinpath("envs", ".env"),
    envvar_prefix_for_dynaconf=False,
)

DATABASE_URL = settings("database_url")
sv_host = settings("sv_host")
sv_port= settings("sv_port")

virustotal_api_key = settings("virustotal_api_key")
whois_api_key = settings("whois_api_key")
geekflare_api_key = settings("geekflare_api_key")
censys_api = settings("censys_api")
alienvault = settings("alienvault")
ipstack = settings("ipstack")