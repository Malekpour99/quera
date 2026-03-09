# https://quera.org/problemset/33038
# ----------------------------------

from typing import Callable

NO_ERROR_MESSAGE = "ok!"


class ExceptionProxy(Exception):

    def __init__(self, msg: str, function: Callable):
        self.msg = msg
        self.function = function


def transform_exceptions(func_ls: list[Callable]) -> list[ExceptionProxy]:
    result: list[ExceptionProxy] = []
    for func in func_ls:
        exception_proxy = ExceptionProxy(
            msg=NO_ERROR_MESSAGE,
            function=func,
        )
        try:
            func()
        except Exception as e:
            exception_proxy.msg = str(e)

        result.append(exception_proxy)

    return result
