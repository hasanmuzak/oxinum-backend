import pytest
import requests
import os
import time

import dotenv
dotenv.load_dotenv()
base_url = os.environ.get("API_URL")


@pytest.mark.order(1)
def test_create_user():
    r = requests.post(base_url + '/user/create-user', json={
        "name": "Hasan",
        "surname": "Muzak",
        "password": "oxinum1",
        "email": "hasanmuzak@yandex.com",
        "created_at": str(round(time.time()*1000))
    })
    assert r.status_code == 200
