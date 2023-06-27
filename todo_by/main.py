#!/usr/bin/env python3

import datetime
import functools
from .utils import _get_version, _compare_semver

def todo_by(date_str, comment=None):
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    now = datetime.date.today()

    if date < now:
        date_str = date.strftime("%b %-d, %Y")
        error_message = f"TODO by {date_str} has passed"
        if comment:
            error_message += f": {comment}"
        raise RuntimeError(error_message)

    def wrapper(f, date_str=date_str, comment=comment):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapped
    return functools.partial(wrapper)

def todo_while(version_str, file, comment=None):
    current_version = _get_version(file)
    comparison = _compare_semver(current_version, version_str)

    if comparison >= 0:
        error_message = f"TODO version requirement '{version_str}' not satisfied by current v{current_version}"
        if comment:
            error_message += f": {comment}"
        raise RuntimeError(error_message)

    def wrapper(f, version_str=version_str, comment=comment):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapped
    return functools.partial(wrapper)
