# CASE_RATE

> This table contains information about case rate and dental treatment plan.

**Primary key:** `CASE_RATE_ID`  
**Columns:** 7  
**Org-specific columns:** 1  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_RATE_ID` | VARCHAR | PK | The unique identifier for a case rate record. |
| 2 | `ACTIVE_YN` | VARCHAR |  | Indicates whether the case is active. Y indicates the case is active. There will be no null value for this column. |
| 3 | `CASE_RATE_TYPE_C_NAME` | VARCHAR | org | The category value representing the type of transplant for the case rate. |
| 4 | `ACCOUNT_ID` | NUMERIC | FK→ | The guarantor account ID associated with this case rate. |
| 5 | `FROM_SVC_DATE` | DATETIME |  | The first service date in the inclusion period for the case rate procedures. |
| 6 | `T0_SVC_DATE` | DATETIME |  | The last service date in the inclusion period for the case rate procedures. |
| 7 | `BATCH_PRC_FLAG_C_NAME` | VARCHAR |  | A flag that indicates the charging status of the case rate record. This flag can be set to indicate that the holding period is complete, the inclusion period is complete, or neither is complete. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [CASE_RATE_ACCT](CASE_RATE_ACCT.md) | `CASE_RATE_ID` | high |
| [CASE_RATE_CVG](CASE_RATE_CVG.md) | `CASE_RATE_ID` | high |

