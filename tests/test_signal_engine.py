from decimal import Decimal

import pytest

from app.signal_engine import calculate_price_signal


def test_momentum_up():
    result = calculate_price_signal(prev_price=Decimal('100.00'), cur_price=Decimal('102.00'))

    assert result == {
        'previous_price': Decimal('100.00'),
        'current_price': Decimal('102.00'),
        'price_change': Decimal('2.00'),
        'price_change_pct': Decimal('2.000'),
        'signal': 'momentum_up'
    }


def test_momentum_down():
    result = calculate_price_signal(prev_price=Decimal('100.00'),
                                cur_price=Decimal('98.00'))

    assert result['signal'] == 'momentum_down'

def test_momentum_neutral():
    result = calculate_price_signal(prev_price=Decimal('100.00'),
                                cur_price=Decimal('100.2'))

    assert result['signal'] == 'neutral'

def test_zero_values():
    with pytest.raises(ValueError):
        calculate_price_signal(prev_price=Decimal('0.00'),
                            cur_price=Decimal('98.00'))
