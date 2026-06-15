# DOCS_RCVD_PHRM_INF

> This table stores the medication dispense pharmacy information.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `PHARM_REF_ID` | VARCHAR |  | This item stores the pharmacy reference identifier. |
| 4 | `PHARM_NAME` | VARCHAR |  | This item stores the pharmacy name. |
| 5 | `PHARM_PHONE_NUM` | VARCHAR |  | This item stores the pharmacy phone number. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

