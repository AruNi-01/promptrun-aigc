from langchain_sql.prompt_search.context import PromptSearchContext
from langchain_sql.prompt_search.llm_answer_chain import _answer_by_llm_chain
from langchain_sql.prompt_search.sql_exec_chain import _exec_sql_chain
from langchain_sql.prompt_search.sql_generate_chain import _generate_sql
from langchain_sql.prompt_search.user_input_deal_chain import _deal_user_input


def find_result_by_sql_langchain(user_input: str) -> str:
    ctx = PromptSearchContext(user_input=user_input)
    _deal_user_input(context=ctx)
    _generate_sql(context=ctx)
    _exec_sql_chain(context=ctx)
    _answer_by_llm_chain(context=ctx)
    return ctx.get_final_result()

