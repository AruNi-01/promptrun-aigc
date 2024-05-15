from typing import Optional


class PromptSearchContext:
    def __init__(self, user_input: str = None):
        self.user_input: str = user_input
        self.dealt_user_input: Optional[str] = None
        self.sql: Optional[str] = None
        self.sql_result: Optional[str] = None
        self.final_result: Optional[str] = None

    def get_final_result(self) -> Optional[str]:
        return self.final_result
