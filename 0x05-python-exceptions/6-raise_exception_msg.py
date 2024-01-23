#!/usr/bin/python3
def raise_exception_msg(message=""):
    class CustomNameError(NameError):
        pass

    raise CustomNameError(message)
