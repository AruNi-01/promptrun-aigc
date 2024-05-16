from typing import Optional, List

from pydantic import BaseModel, Field


class PromptSearchContext:
    def __init__(self, user_input: str = None):
        self.user_input: str = user_input
        self.dealt_user_input: Optional[str] = None
        self.sql: Optional[str] = None
        self.sql_result: Optional[str] = None
        self.final_result: Optional[List[PromptSearchResp]] = None

    def get_final_result(self) -> Optional[str]:
        return self.final_result


class PromptSearchResp(BaseModel):
    id: int = Field(description="id of the prompt")
    title: str = Field(description="title of the prompt")
    intro: str = Field(description="intro of the prompt")
    publish_status: int = Field(description="publish status of the prompt")
    audit_status: int = Field(description="audit status of the prompt")

