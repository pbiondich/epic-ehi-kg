# PR_EST_LETTERS

> This table contains information about the method by which a member received an estimate letter. If this column is blank, a letter was not sent for the estimate.

**Primary key:** `ESTIMATE_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the patient estimate record. |
| 2 | `MC_LETTERS_SENT_C_NAME` | VARCHAR |  | The letters sent category ID for the estimate. Indicates the method by which a member received an estimate letter. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

