from pydantic_settings import BaseSettings


class AppConfigSettings(BaseSettings):
    """应用配置"""
    app_port: int
    app_debug: bool

    """数据库配置"""
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_database: str
