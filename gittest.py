import json
import logging
import logging.config
import os
import re
import time
from hashlib import md5
from typing import List, Optional
from urllib.parse import urlencode

import httpx


def chicken_checkin() -> None:
    """几鸡签到
    """

    logger = logging.getLogger("chicken")

    client = httpx.Client()
    email = os.environ["CHICKEN_MAIL"]
    passwd = os.environ["CHICKEN_PASSWORD"]

    login_resp = client.post(
        "http://j01.space/signin",
        headers={"Content-Type": "application/json;charset=UTF-8"},
        content=json.dumps(
            {"email": email, "passwd": passwd},
            separators=(",", ":")
        )
    )
    logger.info(login_resp.json())

    checkin_resp = client.post(
        "http://j01.space/user/checkin"
    )
    logger.info(checkin_resp.json())
