import pytest
import requests
import os
import time

import dotenv
dotenv.load_dotenv()
base_url = os.environ.get("API_URL")

data = [
    {
        "title": "bitcoin",
        "symbol": "BTCUSDT",
        "logo": "https://cryptologos.cc/logos/bitcoin-btc-logo.svg?v=014"
    },
    {
        "title": "ethereum",
        "symbol": "ETHUSDT",
        "logo": "https://cryptologos.cc/logos/ethereum-eth-logo.svg?v=014"
    },
    {
        "title": "winklink",
        "symbol": "WINUSDT",
        "logo": None
    },
    {
        "title": "ripple",
        "symbol": "XRPUSDT",
        "logo": "https://cryptologos.cc/logos/xrp-xrp-logo.svg?v=014"
    }
]


@pytest.mark.order(1)
def test_create_currency():
    for i in data:
        r = requests.post(base_url + '/currency/create-currency', json=i)
        assert r.status_code == 200


@pytest.mark.order(2)
def test_get_all_currencies():
    for i in data:
        r = requests.get(base_url + '/currency/all')
        assert r.status_code == 200