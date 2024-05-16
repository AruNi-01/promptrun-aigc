from langchain_community.tools import QuerySQLDataBaseTool

from langchain_sql import db
from langchain_sql.prompt_search.context import PromptSearchContext


def _exec_sql_chain(context: PromptSearchContext) -> None:
    """
    执行 SQL，获取到结果
    """
    _execute_query = QuerySQLDataBaseTool(db=db)
    context.sql_result = _execute_query(context.sql)
    print(f"【chain-3】 SQL 执行结果: {context.sql_result}")

