import redis
import uuid
from datetime import datetime
from hashids import Hashids
import os
def getUID():
    hashids = Hashids(salt="Ali Saleh Baker encryption service in github repo",
                      alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    choices = str(uuid.uuid4())[:8]
    uniuqID = "{}{}".format(hashids.encode(
        int(datetime.today().timestamp())), choices)
    return uniuqID

def redisCon():
    r = redis.Redis(host="localhost")
    try:
        r.execute_command("module load /projects/rd_themis/rd_themis.so")
    except:
        print("Already loaded module")
    return r