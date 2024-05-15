from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from langchain_sql import llm
from langchain_sql.prompt_search.context import PromptSearchContext


def _deal_user_input(context: PromptSearchContext) -> None:
    """
    处理用户输入的内容，转成 SQL 提问的内容
    """
    deal_user_input_prompt = PromptTemplate.from_template(
        f"""
        Given the following user requirement, deal it, and generate to sql query text.
        UserRequirement: {context.user_input}
        """
    )

    context.dealt_user_input = deal_user_input_prompt | llm | StrOutputParser()
    print(f"【chain-1】deal_user_input: {context.dealt_user_input}")
