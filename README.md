# NoBroker Strategy Case: Lead Value, Benchmarking and Category Growth

A business strategy case on NoBroker, India's broker-free property platform, built entirely from public information. **Written for a PS-II application**, then updated when the company's own disclosures outdated part of it.

📊 **[Which lead should NoBroker buy?](docs/lead_routing.md)** · [Competitive benchmarking](docs/competitive_benchmarking.md) · [Growth and category expansion](docs/growth_and_category_expansion.md) · [Model (Excel)](model/growth_model.xlsx) · [Sources and assumptions](data/SOURCES.md)

---

## The headline

**A lead is not a lead — there is a 34× spread in what one is worth, depending on the journey it enters.** One primary sale is worth roughly **140 months of a premium subscription**.

| Journey | Value if it completes | Conversion | **Value per lead** |
| --- | ---: | ---: | ---: |
| **Primary sale** | ₹4,20,000 | 2% | **₹8,400** |
| Resale transaction | ₹2,67,000 | 2% | ₹5,340 |
| Home loan referral | ₹53,400 | 5% | ₹2,670 |
| Rental subscription | ₹7,500 | 6% | ₹450 |
| Home service order | ₹700 | 35% | ₹245 |

**Rank the same journeys by conversion rate and the order inverts almost exactly.** A funnel dashboard optimised on conversion points the business at the lowest-value journey — which is why routing beats volume here, and why the metric a growth team reaches for first is the wrong one.

Nearly **90% of users are free**, so any routing improvement applies to that base at **zero acquisition cost**.

## Why this repo changed its own mind

The first version argued, from FY24 filings where **subscriptions were 99% of ₹803 Cr** of revenue, that attaching services to the move event was the biggest lever.

On the founder's FY26 account, **core real estate is down to ~50–55%** and ancillary lines are close to half of revenue, with financial services at 22.4% and growing ~2.5× in a year. That recommendation has been executed. The earlier doc is kept rather than deleted, and [the update](docs/lead_routing.md) says what dated and why.

## Honest about what's assumed

The commission rate is the largest single assumption — a **₹5,600** swing across the quoted 2–4% band, more than the entire value of a rental-subscription lead. **The ranking survives it:** primary sales lead at 2% as well as 4%, asserted as a test. The conversion rates are mine, they are the weakest input, and they are the first thing I would replace with real data.

## Run it

```bash
python -m pytest -q   # 9 tests
```

The tests fail if the premises stop holding — if the value ordering stops inverting the conversion ordering, if the ranking becomes an artefact of the commission band, or if ancillary revenue falls back below 40% and the FY24 argument applies again.

## Related

[Hyderabad housing analytics](https://github.com/f20220970-debug/hyderabad-housing-analytics): resale price prediction (6% median error) and locality clusters with supply gaps — the model behind the "free home-price estimate" idea in the benchmarking doc.

Built by Pavitra Seth from public sources.
