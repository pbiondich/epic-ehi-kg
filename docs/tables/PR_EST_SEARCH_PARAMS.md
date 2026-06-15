# PR_EST_SEARCH_PARAMS

> Contains information about an audited search run in Cost Calculator.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the patient estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SEARCH_RESULTS_CNT` | INTEGER |  | A numeric item for holding the number for successful results found in a Cost Calculator search. |
| 4 | `SEARCH_RANGE` | INTEGER |  | The range in miles that the user searched from their starting zip code. |
| 5 | `SEARCH_ZIP` | VARCHAR |  | The zip code that was used to search for providers. |
| 6 | `SEARCH_LATITUDE` | NUMERIC |  | The latitude value of the search from Cost Calculator. |
| 7 | `SEARCH_LONGITUDE` | NUMERIC |  | The longitude value of the search from Cost Calculator. |
| 8 | `MIN_PRICE` | NUMERIC |  | The lowest price found for the related search parameters. |
| 9 | `MAX_PRICE` | NUMERIC |  | The highest price found for the related search parameters. |
| 10 | `IS_TEST_RUN_YN` | VARCHAR |  | Yes if this cost calculator search was done with a pending template. No otherwise. |
| 11 | `FAIL_REASON_C_NAME` | VARCHAR |  | Why this Cost Calculator search failed to return any results. |
| 12 | `NO_PRICE_ERROR_CNT` | INTEGER |  | How many Cost Calculator results were excluded from this search because we were unable to calculate an allowed amount. |
| 13 | `BENEFITS_ERROR_CNT` | INTEGER |  | How many Cost Calculator search results were excluded from this search because benefits applied a pend code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

