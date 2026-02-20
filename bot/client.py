import time
import hmac
import hashlib
import logging
import requests
import os
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


class BinanceFuturesClient:
    BASE_URL = "https://testnet.binancefuture.com"

    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError("API credentials not found in environment variables.")

    def _sign(self, params: dict):
        query_string = urlencode(params)
        signature = hmac.new(
            self.api_secret.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()
        return signature

    def _headers(self):
        return {
            "X-MBX-APIKEY": self.api_key
        }

    def place_order(self, params: dict):
        endpoint = "/fapi/v1/order"
        url = self.BASE_URL + endpoint

        params["timestamp"] = int(time.time() * 1000)
        params["signature"] = self._sign(params)

        logger.info(f"Sending order request: {params}")

        try:
            response = requests.post(url, headers=self._headers(), params=params)
            logger.info(f"Response status code: {response.status_code}")
            logger.info(f"Response body: {response.text}")

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {str(e)}")
            raise
