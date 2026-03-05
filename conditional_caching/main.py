# https://quera.org/problemset/251438?tab=description
# ---------------------------------------------------

import time
import functools
import threading
from collections import OrderedDict


def conditional_cache(expiry, condition, max_size=5):
    cache_store = OrderedDict()
    lock = threading.Lock()

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not condition(*args, **kwargs):
                return None

            cache_key = (args, frozenset(kwargs.items()))

            with lock:
                if cache_key in cache_store:
                    cached_result, timestamp = cache_store[cache_key]
                    if time.time() - timestamp < expiry:
                        cache_store.move_to_end(cache_key)
                        return cached_result

                result = func(*args, **kwargs)

                cache_store[cache_key] = (result, time.time())

                cache_store.move_to_end(cache_key)

                if len(cache_store) > max_size:
                    cache_store.popitem(last=False)  # Pops the first item
                    # if you want to use below code, you must update the cache_key timestamp
                    # whenever its called and its cached_result is returned
                    # oldest_key = min(cache_store, key=lambda k: cache_store[k][1])
                    # del cache_store[oldest_key]

                return result

        return wrapper

    return decorator
