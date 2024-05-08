import re
from models import Site
import storage

URL_REGEX = "(http(s)?:\\/\\/)?(www\\.)?[-a-zA-Z0-9%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()%_\\+.~#?&\\/=]*)"

def valid_hash(hash: str):
    valid = True
    message = ""

    if len(hash) < 1 or len(hash) > 8:
        valid = False
        message = "Hash must be between 1 and 8 characters long"

    if not hash.isalnum():
        valid = False
        message = "Hash must be an alpha numeric value"

    return valid, message

def valid_new_site(site: Site):
    valid = True
    message = ""

    if not site:
        valid = False
        message = "Site can't be empty"

    url = re.fullmatch(URL_REGEX, site.redirect)
    if not url:
        valid = False
        message = f"{site.redirect} is not a valid URL for redirection"
    
    if site.hash:
        valid, message = valid_hash(site.hash)

        if valid and storage.exists(site.hash):
            valid = False
            message = f"Custom hash: {site.hash} is already taken"

    return valid, message

