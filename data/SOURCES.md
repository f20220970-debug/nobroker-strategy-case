# Sources and assumptions

Every input is a **Fact** with a citation or an **Assumption** with the range tested. Nothing here comes from NoBroker's internal data.

## Facts

| Figure | Value | Source |
| --- | --- | --- |
| FY24 operating revenue | **₹803 Cr**, ~90% from core rental and listings | RoC filings via Entrackr |
| FY24 net loss | **₹411 Cr** | RoC filings via Entrackr |
| FY26 revenue split (founder's account, not independently verified) | core real estate **50–55%**; financial services **22.4%**; home services roughly the rest — ancillary lines **nearly 50%** | Amit Agarwal (co-founder/CEO), Inc42, 2026 |
| Financial services growth | **~2.5×** in the last year | same |
| Real estate transactions | **>1 lakh** in March 2026 | same |
| Home services orders | **~1.5 lakh** in March 2026 | same |
| Primary sales GMV | **₹1,000 Cr** in March 2026 | same |
| Average ticket size | **₹89 lakh** resale, **₹1.4 Cr** primary | same |
| Premium plan price | **~₹3,000 per month per user** | same |
| Share of users on free plans | **nearly 90%** | same |
| Channel-partner commission on primary sales | **2–4%** of deal value; NoBroker says its own take is comparable but does not disclose it | same |
| Profitability | not yet profitable; targeting it within **12–15 months** as of 2026 | same |

FY25 and FY26 audited financials had not been filed at the time of writing, so no total revenue figure exists for either year. The FY26 split above is the founder's characterisation, and the case treats it as such.

## Assumptions

| Assumption | Base | Range tested | Effect |
| --- | --- | --- | --- |
| Commission realised on primary/resale | 3% | 2% – 4% | **₹5,600** swing in value per lead — the largest single assumption |
| Home-loan referral fee | 0.75% of loan | 0.5% – 1.0% | ₹1,780 swing |
| Loan-to-value on a financed purchase | 80% | 60% – 90% | — |
| Months a rental seeker holds a plan | 2.5 | 1 – 4 | ₹270 swing |
| Home service order value / take rate | ₹3,500 / 20% | ₹1,500–8,000 / 10–30% | — |
| Lead-to-completion conversion by journey | 2% primary and resale, 5% loan, 6% subscription, 35% service | — | Directional. These are the weakest numbers in the model and the first thing I would replace with real data |

**The ranking does not depend on the biggest assumption.** Primary sales lead the value-per-lead table at a 2% commission as well as at 4%, which is asserted as a test (`test_the_ranking_is_not_an_artefact_of_the_commission_assumption`).
