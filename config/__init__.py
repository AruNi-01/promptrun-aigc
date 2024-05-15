from dotenv import load_dotenv

from config.app_conf import AppConfigSettings


def _get_app_config() -> AppConfigSettings:
    # 加载 .env 文件，dotenv_path 变量默认是.env
    load_dotenv()
    # 实例化配置模型
    return AppConfigSettings()


# 获取配置
appConf = _get_app_config()
