from decimal import ROUND_HALF_UP, Decimal


def calculate_price_signal(prev_price: Decimal, cur_price: Decimal) -> dict[str, Decimal | str]:

    if prev_price <= 0:
        raise ValueError('prev_price has to be greater than 0')

    price_chg = cur_price - prev_price
    price_pct_chg = price_chg / prev_price * 100

    if price_pct_chg >= 1:
        signal_movement = 'momentum_up'

    elif price_pct_chg <= -1:
        signal_movement = 'momentum_down'
    else:
        signal_movement = 'neutral'

    return {
        'previous_price': prev_price,
        'current_price': cur_price,
        'price_change': price_chg.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        'price_change_pct': price_pct_chg.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP),
        'signal': signal_movement
    }
