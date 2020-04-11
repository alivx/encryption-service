from lib.extra import *
from fastapi import FastAPI, Query
from pydantic import BaseModel, AnyHttpUrl

app = FastAPI()

r = redisCon()


class Item(BaseModel):
    value: str
    password: str = "abcd1234"
    ttl: int = 604800


@app.put("/set/")
async def read_items(item: Item):
    _id = getUID()
    r.execute_command("rd_themis.cset {} {} {}".format(
        _id, item.password, item.value))
    r.expire(_id,item.ttl)
    query_items = {"_id": _id}
    return query_items


@app.get("/get/")
async def read_itemss(_id: str, password: str):
    if _id == None:
        value = "Does not exists, or the value has been expired"
    try:
        value = r.execute_command("rd_themis.cget {} {}".format(_id, password))
    except:
        value = "decryption failed"
    # value = encData("dec", _id, password)
    query_items = {"value": value}
    return query_items
