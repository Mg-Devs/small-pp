import storage
from typing import Union
from validations import valid_hash, valid_new_site
from models import Site
from fastapi import FastAPI, Response, status

app = FastAPI()


@app.get("/{hash}", status_code=301)
def read_root(hash: str, response: Response):
    valid, message = valid_hash(hash)

    if not valid:
        response.status_code = 400
        return {"code": 400, "message": message}

    redirect = storage.get_redirect(hash)

    if not redirect:
        response.status_code = 404
        return {"code": 404, "message": "Redirect Not Found"}

    return {"redirect_to": redirect}


@app.post("/add")
def read_item(site: Site, response: Response):
    valid, message = valid_new_site(site)

    if not valid:
        response.status_code = 400
        return {"code": 400, "message": message}
    
    site = storage.add(site)
    return {"site": site}
