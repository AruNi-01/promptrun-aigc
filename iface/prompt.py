from fastapi import APIRouter

from config import appConf
from langchain_sql import db
from langchain_sql.prompt_search import find_result_by_sql_langchain

prompt_router = APIRouter()


@prompt_router.get("/prompt/{query_str}")
async def say_hello(query_str: str):
    result = find_result_by_sql_langchain(query_str)
    return {"query": f"{query_str}", "result": f"{result}"}


@prompt_router.get("/")
async def root():
    return {"message": "Hello World", "env": f"{appConf}", "DB": f"dialect={db.dialect}, tables={db.get_usable_table_names()}"}
