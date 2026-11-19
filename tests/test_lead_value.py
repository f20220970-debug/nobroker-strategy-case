"""Tests that fail if this case's premises stop holding."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import lead_value as L  # noqa: E402


def test_primary_sale_is_the_most_valuable_lead():
    assert L.ranked()[0].name == "Primary sale"


def test_the_ranking_is_not_an_artefact_of_the_commission_assumption():
    """The whole finding would be worthless if it only held at 4%."""
    assert L.ranking_survives_commission_band() is True


def test_lead_values_span_two_orders_of_magnitude():
    s = L.spread()
    assert s["multiple"] == 34.3
    assert s["best"] == "Primary sale"
    assert s["worst"] == "Home service order"


def test_one_primary_sale_equals_many_years_of_subscription():
    g = L.gross_before_conversion()
    assert g["equivalent_subscription_months"] == 140
    assert g["equivalent_subscriptions"] == 56.0


def test_the_fy24_services_recommendation_has_been_executed():
    """If this ever reverts, the earlier version of this case applies again."""
    v = L.services_argument_is_dated()
    assert v["fy24_subscription_share"] == 0.99
    assert v["fy26_ancillary_share"] >= 0.40
    assert v["fy26_core_real_estate_share"] < 0.60


def test_conversion_ordering_opposes_value_ordering():
    """Why the cheap, high-converting lead is the trap.

    Home services convert best and are worth least; primary sales convert
    worst and are worth most. A funnel optimised on conversion rate alone
    would point the business at exactly the wrong journey.
    """
    by_value = [j.name for j in L.ranked()]
    by_conversion = [j.name for j in sorted(L.journeys(), key=lambda j: -j.conversion)]
    assert by_value[0] == by_conversion[-1]
    assert by_value[-1] == by_conversion[0]


def test_commission_is_the_largest_single_assumption():
    comm = L.swing(L.sensitivity(L.primary, "commission", [0.02, 0.03, 0.04]))
    loan = L.swing(L.sensitivity(L.home_loan, "rate", [0.005, 0.0075, 0.01]))
    months = L.swing(L.sensitivity(L.rental_subscription, "months", [1.0, 2.5, 4.0]))
    assert comm > loan > months


def test_free_base_is_the_zero_cost_lever():
    v = L.free_base_leverage()
    assert v["free_user_share"] == 0.90
    assert v["paid_user_share"] == 0.10


def test_open_questions_are_recorded():
    qs = L.what_i_would_need()
    assert len(qs) >= 5
    assert any("commission" in q.lower() for q in qs)
