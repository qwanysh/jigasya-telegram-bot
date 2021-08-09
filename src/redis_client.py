from redis import Redis

from src import config

redis_client = Redis.from_url(url=config.REDIS_URL)
