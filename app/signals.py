signals = {

    'AAPL' : {

      "symbol": "AAPL",
      "price": 330.78,
      "signal": "momentum_up",
      "confidence": 0.72,
      "timestamp": "2026-10-02T12:00:00Z"
    },

    'MSFT' : {

      "symbol": "MSFT",
      "price": 513.32,
      "signal": "momentum_down",
      "confidence": 0.90,
      "timestamp": "2026-10-02T12:00:00Z"
    },

    'NVDA' : {

      "symbol": "NVDA",
      "price": 231.49,
      "signal": "momentum_up",
      "confidence": 0.60,
      "timestamp": "2026-10-02T12:00:00Z"
    },
}

def all_signals() -> list:
    return list(signals.values())

def search_signal(signal: str) -> dict | None:
    return signals.get(signal.upper(), None)
