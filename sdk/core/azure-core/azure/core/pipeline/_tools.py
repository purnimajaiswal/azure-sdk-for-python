# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

def await_result(func, *args, **kwargs):
    """If func returns an awaitable, raise that this runner can't handle it."""
    result = func(*args, **kwargs)
    if hasattr(result, "__await__"):
        raise TypeError(
            "Policy {} returned awaitable object in non-async pipeline.".format(func)
        )
    return result


def case_insensitive_dict(*args, **kwargs):
    """Return a case-insensitive dict from a structure that a dict would have accepted.

    Rational is I don't want to re-implement this, but I don't want
    to assume "requests" or "aiohttp" are installed either.
    So I use the one from "requests" or the one from "aiohttp" ("multidict")
    If one day this library is used in an HTTP context without "requests" nor "aiohttp" installed,
    we can add "multidict" as a dependency or re-implement our own.
    """
    try:
        from requests.structures import CaseInsensitiveDict

        return CaseInsensitiveDict(*args, **kwargs)
    except ImportError:
        pass
    try:
        # multidict is installed by aiohttp
        from multidict import CIMultiDict

        return CIMultiDict(*args, **kwargs)
    except ImportError:
        raise ValueError(
            "Neither 'requests' or 'multidict' are installed and no case-insensitive dict impl have been found"
        )