# Example of a custom module to be imported

import re


def validate_email(email_ds):
    if len(email_ds) > 7:
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email_ds))
