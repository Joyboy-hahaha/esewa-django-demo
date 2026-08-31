import os
import base64
import hashlib
import hmac


ESEWA_SECRET_KEY = os.environ.get("ESEWA_SECRET_KEY")


def generate_signature(message):
    key = ESEWA_SECRET_KEY.encode("utf-8")
    message = message.encode("utf-8")

    digest = hmac.new(
        key,
        message,
        hashlib.sha256
    ).digest()

    return base64.b64encode(digest).decode("utf-8")