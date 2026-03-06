import argparse

from bot.orders import place_order
from bot.validators import validate_side, validate_type, validate_price
from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

    side = validate_side(args.side)
    order_type = validate_type(args.type)

    validate_price(order_type, args.price)

    print("Order Request Summary")
    print("----------------------")
    print(args.symbol, side, order_type, args.quantity, args.price)

    response = place_order(
        args.symbol,
        side,
        order_type,
        args.quantity,
        args.price
    )

    print("\nOrder Response")
    print("----------------------")
    print("Order ID:", response.get("orderId"))
    print("Status:", response.get("status"))
    print("Executed Qty:", response.get("executedQty"))

except Exception as e:

    print("Error:", str(e))