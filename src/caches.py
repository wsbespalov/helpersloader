import redis

cache_host = "localhost"
cache_port = 6379
cache_db = 3
cache_charset = "utf-8"
cache_decode_responses = True
helpers_collection_name = "helpers_collection"

cache = redis.StrictRedis(
    host=cache_host,
    port=cache_port,
    db=cache_db,
    charset=cache_charset,
    decode_responses=cache_decode_responses
)

def clear_helpers_collection():
    if not cache.exists(helpers_collection_name):
        return True
    try:
        cache.delete(helpers_collection_name)
    except Exception as ex:
        print("[e] Get an exception while load helpers from cache {}".format(ex))

def cache_push_helpers(element):
    try:
        cache.rpush(helpers_collection_name, element)
    except Exception as ex:
        print("[e] Get an exception while load helpers from cache {}".format(ex))

def push_helpers_collection(helpers):
    helpers = [helpers] if not isinstance(helpers, list) else helpers
    for helper in helpers:
        cache_push_helpers(helper)

def get_helpers_collection():
    helpers = []
    if not cache.exists(helpers_collection_name):
        return helpers
    try:
        helpers = cache.lrange(helpers_collection_name, 0, -1)
        if helpers is not None:
            if isinstance(helpers, list):
                return helpers
    except Exception as ex:
        print("[e] Get an exception while load helpers from cache {}".format(ex))
    return helpers