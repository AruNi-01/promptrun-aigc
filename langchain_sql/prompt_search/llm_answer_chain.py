from langchain_sql.prompt_search.context import PromptSearchContext


def _answer_by_llm_chain(context: PromptSearchContext) -> None:
    """
    根据 SQL 结果回答问题，以获取最后的结果
    """

