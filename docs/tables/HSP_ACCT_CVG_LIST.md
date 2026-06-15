# HSP_ACCT_CVG_LIST

> This table contains hospital account and PB visit coverage list information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account. |
| 2 | `LINE` | INTEGER | PK | This column stores the filing order for the hospital account. For example, a LINE of 2 represents the second coverage in the filing order. |
| 3 | `COVERAGE_ID` | NUMERIC | FK→ | This column stores the unique identifier for the coverage associated with the hospital account. |
| 4 | `CVG_IGNR_PRIM_PAY_YN` | VARCHAR |  | This item stores whether the coverage was ignored for being assigned as primary payer. Typically the first coverage in the coverage list is used for primary payer, but a subsequent coverage may be assigned in some cases instead. |
| 5 | `CVG_IGNR_RSN_C_NAME` | VARCHAR |  | This item stores the reason why the coverage was ignored for primary payer. Typically the first coverage in the coverage list is used to determine primary payer, but a subsequent coverage may be assigned in some cases instead. |
| 6 | `CVG_TIMELY_FILING_DATE` | DATETIME |  | This item stores the timely filing date for the coverage. The date is updated as the HAR changes and remains populated after the HAR is closed for reporting purposes. The date stamped is the earliest timely filing date from any active, non-closed buckets for this coverage. If no buckets are active, for primary coverages the prebilled bucket is used to calculate the expected timely filing. For secondary coverages with non active buckets, the NRP deadline is used from the previous coverage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

