import uuid
import base64
import urllib
import hashlib

def generate_key():
    """
    generates a uuid, encodes it with base32 and strips it's padding.
    this reduces the string size from 32 to 26 chars.
    """
    return base64.b32encode(uuid.uuid4().bytes).strip('=').lower()

def gravatar(email):
    gravatar_url = "https://secure.gravatar.com/avatar?"
    gravatar_url += urllib.urlencode({'gravatar_id': hashlib.md5(email.encode("utf8").lower()).hexdigest(), 'd': 'https://www.blossom.io/static/img/ui/blank-avatar.gif'})
    return gravatar_url

def generate_name_from_email(email):
    """
    use email to generate a user name
    by replacing dots with spaces and then titlecases words
    """
    return " ".join(email.split('@')[0].split('.')).title()
