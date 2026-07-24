from decimal import Decimal, ROUND_HALF_UP


CURRENCY_QUANTUM = Decimal('0.01')


def calculate_unit_price(product, option):
    return (product.price * option.coefficient).quantize(
        CURRENCY_QUANTUM, rounding=ROUND_HALF_UP)
