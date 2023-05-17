#!/usr/bin/env python3

import datetime
import functools

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
