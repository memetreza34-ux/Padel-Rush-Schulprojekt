#!/usr/bin/env python3
"""Reproduzierbare Szenariorechnung PADEL RUSH, fiktives Schulprojekt.

Aufruf: python3 scripts/validate_financial_model.py
Keine externen Bibliotheken erforderlich. Alle Preise und Kosten sind Annahmen.
"""
from dataclasses import dataclass

VAT = 1.19                 # Vereinfachte Schulannahme
PAYMENT_FEE = 0.02         # Anteil vom Bruttoumsatz
WEAR_PER_COURT_H = 0.50
MONTH_DAYS = 30
COURTS = 4
HOURS_PER_DAY = 14
FIXED_MONTH_OUTFLOW = 20500.0

@dataclass(frozen=True)
class Offer:
    gross: float
    hours: float
    other_direct: float

    def direct(self):
        return self.gross * PAYMENT_FEE + self.hours * WEAR_PER_COURT_H + self.other_direct

OFFERS = {
    "starter": Offer(4 * 29, 1.5, 45 + 4),
    "academy": Offer(2 * 45, 1, 35 + 2),
    "social": Offer(8 * 18, 2 * 1.5, 15 + 6),
    "league": Offer(16 * 129, 28 * 1.5, 120 + 80 + 20),
    "tournament": Offer(32 * 35, 4 * 4, 160 + 80 + 40),
    "business": Offer(599, 2 * 3, 90 + 45 + 48 + 12),
}
# Modellmonat mit vier organisierten Eventwochen; Liga anteilig 4/7 einer Saison.
UNITS = {"starter": 8, "academy": 16, "social": 8,
         "league": 4 / 7, "tournament": 1, "business": 4}

def monthly(regular_court_price=34.0, occupancy=0.45):
    capacity = COURTS * HOURS_PER_DAY * MONTH_DAYS
    occupied = capacity * occupancy
    event_hours = sum(UNITS[k] * v.hours for k, v in OFFERS.items())
    regular_hours = occupied - event_hours
    if regular_hours < 0:
        raise ValueError("Mehr Eventstunden als verkaufte Courtstunden")
    event_gross = sum(UNITS[k] * v.gross for k, v in OFFERS.items())
    event_cost = sum(UNITS[k] * v.direct() for k, v in OFFERS.items())
    court_gross = regular_hours * regular_court_price
    court_cost = court_gross * PAYMENT_FEE + regular_hours * WEAR_PER_COURT_H
    total_net = (event_gross + court_gross) / VAT
    total_direct = event_cost + court_cost
    surplus = total_net - total_direct - FIXED_MONTH_OUTFLOW
    return capacity, occupied, event_hours, regular_hours, total_net, total_direct, surplus

def verify():
    assert sum((800, 160, 260, 55, 90, 105, 90, 40)) == 1600
    assert abs(OFFERS["league"].hours - 42) < 1e-10
    assert abs(sum(UNITS[k] * v.hours for k, v in OFFERS.items()) - 116) < 1e-10
    expected = (1680, 756, 116, 640, 25189.4357743, 3315.22285714, 1374.21291717)
    actual = monthly()
    for a, e in zip(actual, expected):
        assert abs(a - e) < 0.011, (a, e)
    assert abs(monthly(32)[-1] - 324.182665066) < 0.011
    assert abs(monthly(36)[-1] - 2424.243169268) < 0.011
    assert abs((28 + 40) / 2 - 34) < 1e-10
    assert abs(28 + (40 - 28) * (2 / 3) - 36) < 1e-10
    print("Plausibilitaetspruefung bestanden (alle Werte nur Schulannahmen).")
    print("Courtstunden: verfuegbar {:.0f}, belegt {:.0f}, Events {:.0f}, normal {:.0f}".format(*actual[:4]))
    print("Modell-Nettoerloese: {:.2f} EUR; direkte Kosten: {:.2f} EUR".format(actual[4], actual[5]))
    for price in (32, 34, 36):
        print("Regulaerer Ø-Preis {:.0f} EUR: kalkulierter Ueberschuss {:.2f} EUR".format(price, monthly(price)[-1]))

if __name__ == "__main__":
    verify()
