# Which lead should NoBroker buy?

**An update to [the growth and category case](growth_and_category_expansion.md) in this repo.** That version argued, from FY24 filings where subscriptions were 99% of ₹803 Cr of revenue, that attaching services to the move event was the biggest lever on revenue per customer.

**That argument has dated, and I'd rather say so than leave it standing.** On the founder's FY26 account, core real estate is down to roughly 50–55% of revenue and ancillary lines — financial services at 22.4%, home services most of the rest — are already close to half. Financial services grew about 2.5× in a year. The structural recommendation has been executed. So the interesting question moved.

---

## The finding

A lead is not a lead. Taking the published ticket sizes and the quoted 2–4% channel-partner commission band, and applying my own conversion assumptions:

| Journey | Value if it completes | Conversion | **Value per lead** |
| --- | ---: | ---: | ---: |
| **Primary sale** | ₹4,20,000 | 2% | **₹8,400** |
| Resale transaction | ₹2,67,000 | 2% | ₹5,340 |
| Home loan referral | ₹53,400 | 5% | ₹2,670 |
| Rental subscription | ₹7,500 | 6% | ₹450 |
| Home service order | ₹700 | 35% | ₹245 |

**A 34× spread between the best and worst lead.** Put the other way: **one primary sale is worth about 140 months of a premium subscription** — nearly twelve years of someone paying ₹3,000 a month.

The old version of this case modelled one undifferentiated funnel of "leads" and asked how to get more of them. That was the mistake. **At a 34× spread, routing beats volume.**

## The part that makes it uncomfortable

Rank the same journeys by conversion rate instead, and the order inverts almost exactly. Home services convert best (35%) and are worth least. Primary sales convert worst (2%) and are worth most.

**A funnel dashboard optimised on conversion rate points the business at precisely the wrong journey** — and conversion rate is the metric a growth team looks at first. This is asserted as a test in `tests/test_lead_value.py`, because it is the whole argument.

## Where the cheapest revenue is

**Nearly 90% of NoBroker's users are free.** Any improvement in how a seeker is routed applies to that base at zero acquisition cost. Before buying leads in the highest-value journey, the cheaper experiment is to find out which journey the free base is already in and whether they are being pointed at the right one.

Concretely: a renter is a renter today and a buyer in three years, and a resale buyer is a home-loan lead at the same moment. The question is whether NoBroker knows which journey a user is in **at acquisition**, or only after they have been routed.

## Is this an artefact of my assumptions?

The commission rate is the largest single assumption, worth a **₹5,600** swing in value per lead across the quoted 2–4% band — more than the entire value of a rental-subscription lead. So it is worth checking whether the conclusion survives it.

**It does.** Primary sales top the table at 2% as well as at 4%. That is enforced as a test, because a finding that only holds at the top of a band is not a finding.

What I am **not** claiming: that the conversion rates are right. They are assumptions, they are the weakest numbers here, and they are the first thing I would replace with real data. If primary-sale leads convert at a tenth of my assumption, the ranking changes.

## What I would want before acting on this

1. **Actual realised commission** on primary and resale, rather than the channel-partner band.
2. **Lead-to-transaction conversion by journey.** My figures are assumptions and they drive the ranking as much as value does.
3. **Home-loan attach rate to resale leads**, and the referral fee per disbursal.
4. **Whether a seeker's journey is known at acquisition** or inferred later — this decides whether routing is a targeting problem or a product problem.
5. **Cost per lead by journey.** A 34× value spread only matters if acquisition cost does not spread the same way. If primary-sale leads cost 34× more, there is no arbitrage and the right answer is the boring one.

That last question is the one I would ask first, and it is the one that could invalidate everything above.

## What this does not claim

- The FY26 split is the founder's characterisation in an interview, not audited. FY25 and FY26 financials had not been filed.
- No view on NoBroker's actual acquisition costs, which I cannot see and which decide whether this is actionable.
- Conversion rates are mine, directional, and the weakest input in the model.
- This supersedes the services-attach recommendation in this repo's earlier doc on the strategic question, but the category ranking and the conversion tests there still stand on their own.
