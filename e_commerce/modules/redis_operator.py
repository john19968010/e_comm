from functools import wraps

import redis
from django.conf import settings


class RedisOperator:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            orig = super(RedisOperator, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        redis_info = settings.REDIS_INFO
        self.pool = redis.ConnectionPool(host=redis_info["host"], port=redis_info["port"])
        self.r = None

    def handle_redis_operator_exception(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            try:
                return_result = f(*args, **kwargs)
            except Exception as e:
                return_result = {"status": False, "res": str(e)}
            finally:
                return return_result

        return decorated

    def has_connected(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            self = args[0]
            if self.r is None:
                self.r = redis.Redis(connection_pool=self.pool)
                self.r.ping()
            return f(*args, **kwargs)

        return decorated

    @handle_redis_operator_exception
    @has_connected
    def get_key(self, key):
        value = self.r.get(key)
        return {"status": True, "res": value}

    @handle_redis_operator_exception
    @has_connected
    def set_key(self, key, value):
        self.r.set(key, value)
        return {"status": True, "res": f"Set {key} - {value} successfully"}

    @handle_redis_operator_exception
    @has_connected
    def delete_key(self, key):
        self.r.delete(key)
        return {"status": True, "res": f"Delete {key} successfully"}

    @handle_redis_operator_exception
    @has_connected
    def list_keys(self, pattern):
        keys = [str(key, encoding="utf-8") for key in self.r.scan_iter(pattern)]
        return {"status": True, "res": keys}
