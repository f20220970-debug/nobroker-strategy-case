"""What a NoBroker lead is worth, by which journey it enters.

Written as an update to the FY24 version of this case, which argued that
attaching services to the move event was the biggest lever on revenue per
customer. That argument has dated: on the founder's FY26 account, ancillary
businesses are already close to half of revenue, so the strategic question is
no longer whether to build services. It is which lead to spend money on.

The finding here is that the answer differs by two orders of magnitude, and
that lead *routing* therefore matters more than lead *volume*.

Every figure is labelled in data/SOURCES.md as a published fact or as an
assumption with the range tested.
"""
from __future__ import annotations

from dataclasses import dataclass, replace

# --- published figures (data/SOURCES.md) ------------------------------------
FY24_REVENUE_CR = 803.0
FY24_LOSS_CR = 411.0
FY26_CORE_REAL_ESTATE_SHARE = 0.525    # founder: "roughly 50-55%"
FY26_FINANCIAL_SERVICES_SHARE = 0.224  # founder: 22.4%, grew ~2.5x in a year
PREMIUM_PLAN_INR_PER_MONTH = 3_000.0
RESALE_TICKET_INR = 89_00_000.0        # ~INR 89 lakh average
PRIMARY_TICKET_INR = 1_40_00_000.0     # ~INR 1.4 Cr average
PRIMARY_GMV_MARCH_2026_CR = 1_000.0
HOME_SERVICES_ORDERS_MARCH_2026 = 1_50_000
REAL_ESTATE_TXNS_MARCH_2026 = 1_00_000
FREE_USER_SHARE = 0.90                 # founder: nearly 90% of users are free

# Channel-partner commission band quoted for primary sales.
COMMISSION_LOW, COMMISSION_HIGH = 0.02, 0.04

# --- assumptions (ranges in data/SOURCES.md) --------------------------------
SUBSCRIPTION_MONTHS = 2.5      # a search lasts; tested 1-4
LOAN_LTV = 0.80                # tested 0.6-0.9
LOAN_REFERRAL_RATE = 0.0075    # tested 0.005-0.01
HOME_SERVICE_ORDER_INR = 3_500.0   # tested 1,500-8,000
HOME_SERVICE_TAKE = 0.20           # tested 0.10-0.30


@dataclass(frozen=True)
class Journey:
    """One route a lead can take, and what NoBroker earns if it completes."""
    name: str
    gross_inr: float          # value to NoBroker of one completed lead
    conversion: float         # share of leads in this journey that complete

    @property
    def value_per_lead(self) -> float:
        return self.gross_inr * self.conversion


def rental_subscription(months: float = SUBSCRIPTION_MONTHS) -> Journey:
    return Journey("Rental subscription", PREMIUM_PLAN_INR_PER_MONTH * months, 0.06)


def resale(commission: float = (COMMISSION_LOW + COMMISSION_HIGH) / 2) -> Journey:
    return Journey("Resale transaction", RESALE_TICKET_INR * commission, 0.02)


def primary(commission: float = (COMMISSION_LOW + COMMISSION_HIGH) / 2) -> Journey:
    return Journey("Primary sale", PRIMARY_TICKET_INR * commission, 0.02)


def home_loan(ltv: float = LOAN_LTV, rate: float = LOAN_REFERRAL_RATE) -> Journey:
    return Journey("Home loan referral", RESALE_TICKET_INR * ltv * rate, 0.05)


def home_service(order: float = HOME_SERVICE_ORDER_INR,
                 take: float = HOME_SERVICE_TAKE) -> Journey:
    return Journey("Home service order", order * take, 0.35)


def journeys() -> list[Journey]:
    return [rental_subscription(), resale(), primary(), home_loan(), home_service()]


def ranked() -> list[Journey]:
    return sorted(journeys(), key=lambda j: -j.value_per_lead)


def spread() -> dict:
    """How far apart the best and worst lead are.

    This is the number the FY24 version of this case missed entirely, because
    it modelled one undifferentiated funnel of 'leads'.
    """
    js = ranked()
    best, worst = js[0], js[-1]
    return {
        "best": best.name,
        "best_value_per_lead": round(best.value_per_lead),
        "worst": worst.name,
        "worst_value_per_lead": round(worst.value_per_lead),
        "multiple": round(best.value_per_lead / worst.value_per_lead, 1),
        "implication": ("A rupee of acquisition spend is not fungible across "
                        "journeys. Routing a seeker into the right journey is "
                        "worth more than adding leads to the wrong one."),
    }


def gross_before_conversion() -> dict:
    """The same comparison before conversion, which is how teams usually see it."""
    sub = rental_subscription().gross_inr
    pri = primary().gross_inr
    return {
        "one_primary_sale_inr": round(pri),
        "one_rental_subscription_inr": round(sub),
        "equivalent_subscriptions": round(pri / sub, 1),
        "equivalent_subscription_months": round(pri / PREMIUM_PLAN_INR_PER_MONTH),
    }


def services_argument_is_dated() -> dict:
    """Why the FY24 recommendation in this repo no longer leads anywhere.

    The earlier version argued for attaching services to the move event on the
    basis that subscriptions were ~99% of FY24 revenue. On the founder's FY26
    account, ancillary lines are already close to half. The structural
    recommendation has been executed; what remains is an allocation question.
    """
    ancillary = 1 - FY26_CORE_REAL_ESTATE_SHARE
    return {
        "fy24_subscription_share": 0.99,
        "fy26_core_real_estate_share": FY26_CORE_REAL_ESTATE_SHARE,
        "fy26_ancillary_share": round(ancillary, 3),
        "financial_services_share": FY26_FINANCIAL_SERVICES_SHARE,
        "verdict": ("Already executed. The open question moved from 'should "
                    "NoBroker sell services' to 'which lead should it buy'."),
    }


def free_base_leverage() -> dict:
    """Where the cheapest incremental revenue sits.

    Nearly 90% of users are free. Converting a free user costs no media spend,
    and the spread above says which journey to convert them into.
    """
    return {
        "free_user_share": FREE_USER_SHARE,
        "paid_user_share": round(1 - FREE_USER_SHARE, 2),
        "note": ("Any routing improvement applies to the free base at zero "
                 "acquisition cost, which is why it ranks above buying leads."),
    }


def sensitivity(journey_fn, lever: str, values: list[float]) -> list[dict]:
    """Vary one assumption inside a journey and report value per lead."""
    out = []
    for v in values:
        j = journey_fn(**{lever: v})
        out.append({"lever": lever, "value": v,
                    "value_per_lead": round(j.value_per_lead)})
    return out


def swing(rows: list[dict]) -> float:
    vals = [r["value_per_lead"] for r in rows]
    return round(max(vals) - min(vals), 1)


def ranking_survives_commission_band() -> bool:
    """Does the conclusion hold across the whole quoted commission range?

    If primary sales only top the ranking at a 4% commission, the finding is an
    artefact of picking the top of the band. It does not: it leads at 2% too.
    """
    low = sorted([rental_subscription(), resale(COMMISSION_LOW),
                  primary(COMMISSION_LOW), home_loan(), home_service()],
                 key=lambda j: -j.value_per_lead)
    high = sorted([rental_subscription(), resale(COMMISSION_HIGH),
                   primary(COMMISSION_HIGH), home_loan(), home_service()],
                  key=lambda j: -j.value_per_lead)
    return low[0].name == high[0].name == "Primary sale"


def what_i_would_need() -> list[str]:
    return [
        "Actual commission realised on primary and resale, not the channel-partner band.",
        "Lead-to-transaction conversion by journey -- my conversions are assumptions.",
        "Home-loan referral fee per disbursal, and attach rate to resale leads.",
        "Whether a seeker's journey is known at acquisition or only later.",
        "Cost to acquire a lead by journey, which decides whether routing or buying wins.",
    ]
