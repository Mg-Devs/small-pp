import time
from models import Site

# Memory Storage
__hashes = dict()
BASE_62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encode_b62(num: int) -> str:
    hash = []
    base = len(BASE_62)
    if num == 0:
        return BASE_62[0]

    while num:
        num, rem = divmod(num, base)
        hash.append(BASE_62[rem])

    hash.reverse()
    return ''.join(hash)

def generetate_hash(url: str) -> str:
    '''This is Definitevly a bad way to generate hashes 
       however I think this might work on the mean time'''

    l = len(url)
    p = encode_b62(l + int(time.time()))

    while exists(p):
        p = encode_b62(l + int(time.time()))

    return p

def exists(hash: str) -> bool:
    if __hashes.get(hash):
        return True
    else:
        return False

def add(site: Site) -> Site:
    if not site.hash:
       site.hash = generetate_hash(site.redirect)

    __hashes[site.hash] = site.redirect

    return site

def get_redirect(hash: str):
    return __hashes.get(hash)
