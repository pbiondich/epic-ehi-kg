# UCL_MEA

> Universal Charge's MEA info

**Primary key:** `UCL_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `UCL_ID` | VARCHAR | PK FK→ | The unique ID associated with the charge record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MEA_TEST_C_NAME` | VARCHAR | org | MEA test for the charge |
| 4 | `MEA_RESULT` | NUMERIC |  | MEA test result for the charge |
| 5 | `MEA_PERFORMED_DATE` | DATETIME |  | The date that the test was performed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `UCL_ID` | [CLARITY_UCL](CLARITY_UCL.md) | sole_pk | high |

