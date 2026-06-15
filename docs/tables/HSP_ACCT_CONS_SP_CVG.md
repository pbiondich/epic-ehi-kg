# HSP_ACCT_CONS_SP_CVG

> This table contains Consolidated Self Pay coverage information from the Hospital Accounts Receivable master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the hosp acct record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAYER_NAME` | VARCHAR |  | The name of the coverage payer. |
| 4 | `PLAN_NAME` | VARCHAR |  | The name of the coverage plan. |
| 5 | `SOURCE_CVG_IDENT` | VARCHAR |  | The source system's coverage ID. |
| 6 | `SUBSCRIBER_NUM` | VARCHAR |  | The unique ID of the subscriber for this coverage. |
| 7 | `SUBSCRIBER_NAME` | VARCHAR |  | The name of the subscriber for this coverage. |
| 8 | `PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 9 | `MEMBER_NUM` | VARCHAR |  | The member ID of the coverage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

