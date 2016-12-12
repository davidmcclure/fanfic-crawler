

from .config import Config


config = Config.from_env()

session = config.build_sqla_session()

redis = config.build_redis()
