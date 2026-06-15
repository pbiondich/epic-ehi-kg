# HSPC_BENEFIT_PRDS

> This table contains hospice benefit period information.

**Primary key:** `CVG_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HSPC_START_DT` | DATETIME |  | This item stores the start date for any hospice benefit periods. |
| 4 | `HSPC_END_DT` | DATETIME |  | This item stores the end date for any hospice benefit periods. |
| 5 | `HSPC_CTI_STATUS_C_NAME` | VARCHAR | org | This item stores the signature status of the certificate of terminal illness for the hospice benefit period. |
| 6 | `HSPC_CTI_SIGN_DT` | DATETIME |  | This item stores the date that the certificate of terminal illness (CTI) was signed for each hospice benefit period. |
| 7 | `HSPC_COMMENTS` | VARCHAR |  | Free text comments about hospice benefit periods. Could be used to indicate where the patient received care for this benefit period, if at an outside agency. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |

