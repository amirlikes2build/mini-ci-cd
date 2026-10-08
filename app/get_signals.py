from app.raw_prices import RAW_PRICES
from app.signal_engine import calculate_price_signal


def build_signal_from_raw_price(raw_price: dict) -> dict:
    signal = calculate_price_signal(
        ticker=raw_price["ticker"],
        prev_price=raw_price["prev_price"],
        cur_price=raw_price["cur_price"],
    )

    signal["timestamp"] = raw_price["timestamp"]

    return signal


def get_all_signals() -> list[dict]:
    return [build_signal_from_raw_price(raw_price) for raw_price in RAW_PRICES.values()]


def get_signal_by_ticker(ticker: str) -> dict | None:
    raw_price = RAW_PRICES.get(ticker.upper())

    if raw_price is None:
        return None

    return build_signal_from_raw_price(raw_price)
