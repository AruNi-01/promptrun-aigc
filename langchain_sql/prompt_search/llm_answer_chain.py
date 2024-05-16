from typing import List

from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.prompts import PromptTemplate

from langchain_sql import llm
from langchain_sql.prompt_search.context import PromptSearchContext, PromptSearchResp


def _answer_by_llm_chain(context: PromptSearchContext) -> None:
    """
    根据 SQL 结果回答问题，以获取最后的结果
    """
    _parser = PydanticOutputParser(pydantic_object=List[PromptSearchResp])

    _prompt = PromptTemplate(
        template="according sql result, format it.\n{format_instructions}\n{sql_result}\n",
        input_variables=["sql_result"],
        partial_variables={"format_instructions": _parser.get_format_instructions()},
    )

    output = llm(_prompt.format_prompt(sql_result=context.sql_result))
    context.final_result = _parser.parse(output)
    print(f"【chain-4】 final_result: {context.final_result}")
