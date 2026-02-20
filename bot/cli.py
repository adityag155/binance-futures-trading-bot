import argparse
import logging
from bot.client import BinanceFuturesClient
from bot.orders import create_order_payload
from bot.logging_config import setup_logging


def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    try:
        client = BinanceFuturesClient()

        payload = create_order_payload(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n===== Order Request Summary =====")
        print(payload)

        response = client.place_order(payload)

        print("\n===== Order Response =====")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Quantity: {response.get('executedQty')}")
        print(f"Average Price: {response.get('avgPrice', 'N/A')}")

        print("\nOrder placed successfully.")

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        print("\nOrder failed.")
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
