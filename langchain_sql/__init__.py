from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI

from config import appConf

db = SQLDatabase.from_uri(
    f"mysql+pymysql://{appConf.db_user}:{appConf.db_password}@{appConf.db_host}:{appConf.db_port}/{appConf.db_database}"
)

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

