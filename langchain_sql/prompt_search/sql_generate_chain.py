from langchain.chains.sql_database.query import create_sql_query_chain

from langchain_sql import llm, db
from langchain_sql.prompt_search.context import PromptSearchContext


def _generate_sql(context: PromptSearchContext) -> None:
    """
    根据 SQL 描述，生成 SQL
    """
    _chain = create_sql_query_chain(llm, db)
    _prompt = context.dealt_user_input
    context.sql = _chain.invoke({"question": context.user_input})
    print(f"【chain-2】 生成的 SQL: {context.sql}")
