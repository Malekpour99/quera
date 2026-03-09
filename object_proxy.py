# https://quera.org/problemset/21208
# ----------------------------------

from collections import defaultdict
from typing import Any, Optional

INVALID_METHOD_CALL_MESSAGE = "No Such Method"


class Proxy:
    def __init__(self, obj: object) -> None:
        self._obj = obj
        self._call_counts: defaultdict[str, int] = defaultdict(int)
        self._last_invoked_method: Optional[str] = None

    def __getattr__(self, name: Any) -> Any:
        if hasattr(self._obj, name):
            attr = getattr(self._obj, name)

            # for method, wrap it to track calls
            if callable(attr):

                def wrapped_method(*args, **kwargs):
                    self._last_invoked_method = name
                    self._call_counts[name] += 1
                    # Call the actual method
                    return attr(*args, **kwargs)

                return wrapped_method
            else:
                # for attribute, return it directly
                return attr
        else:
            raise Exception(INVALID_METHOD_CALL_MESSAGE)

    def last_invoked_method(self) -> str:
        if not self._last_invoked_method:
            raise Exception(INVALID_METHOD_CALL_MESSAGE)

        return self._last_invoked_method

    def count_of_calls(self, method_name: str) -> int:
        return self._call_counts.get(method_name, 0)

    def was_called(self, method_name: str) -> bool:
        return method_name in self._call_counts
