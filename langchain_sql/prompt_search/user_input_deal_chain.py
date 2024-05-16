from langchain.chains.sql_database.query import create_sql_query_chain
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from langchain_sql import llm
from langchain_sql.prompt_search.context import PromptSearchContext


def _deal_user_input(context: PromptSearchContext) -> None:
    """
    处理用户输入的内容，转成 SQL 提问的内容
    """
    _prompt = PromptTemplate.from_template(
        """
        给定以下用户需求，将其作为条件处理，所有数据都在‘Prompt’数据库表中，您需要将其生成SQL描述。
        具体来说，一般用户需求中会提到关键词，你需要先合理的拆解这些关键词，然后匹配到prompt标题或简介上。
        另外，查询条件除了title和intro外，还应过滤publish_status为上架（1），audit_status为审核通过（2）。
        除此之外，不要附带其他任何条件。
        
        例如：用户需求=‘我想写关于计算机的广告词。’，先将关键词拆解成计算机、广告，然后您需要生成如下的SQL描述：
        ‘查找出标题title包含计算机或广告，或者简介intro包含计算机或广告的prompt，另外过滤publish_status为上架（1），audit_status为审核通过（2）。’
        
        用户需求: {user_input}
        """
    )

    _chain = _prompt | llm | StrOutputParser()
    context.dealt_user_input = _chain.invoke({"user_input": context.user_input})

    print(f"【chain-1】 处理过的用户输入（SQL Query）: {context.dealt_user_input}")
