# dukeo/services/risk.py
"""
Calcoli di rischio usati dai test e dal webhook.
"""

def calc_position_size(atr: float, balance: float, risk_pct: float) -> float:
    """
    Calcola la dimensione della posizione in unità.
    :param atr:    Valore Average True Range (mock o reale)
    :param balance: Bilancio totale
    :param risk_pct: Rischio per trade come percentuale (es. 2 → 2 %)
    :return: Quantità di asset da acquistare/vendere
    """
    return (balance * risk_pct) / atr


def get_mock_atr() -> float:
    """
    Restituisce un valore ATR fittizio (utilizzato dai test).
    """
    return 100.0


__all__ = ["calc_position_size", "get_mock_atr"]

