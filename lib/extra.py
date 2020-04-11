import redis
import uuid
from datetime import datetime
from hashids import Hashids
import os
def getUID():
    hashids = Hashids(salt="lorem ipsum dolor sit amet",
                      alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    choices = str(uuid.uuid4())[:8]
    uniuqID = "{}{}".format(hashids.encode(
        int(datetime.today().timestamp())), choices)
    return uniuqID

def redisCon():
    r = redis.Redis(host="localhost")
    try:
        r.execute_command("module load {}/lib/rd_themis.so".format(os.getcwd()))
    except:
        print("Already loaded module")
    return r