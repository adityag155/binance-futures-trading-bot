from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


def create_order_payload(symbol, side, order_type, quantity, price=None):
    side = validate_side(side)
    order_type = validate_order_type(order_type)
    quantity = validate_quantity(quantity)
    price = validate_price(order_type, price)

    payload = {
        "symbol": symbol.upper(),
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        payload["price"] = price
        payload["timeInForce"] = "GTC"

    return payload
