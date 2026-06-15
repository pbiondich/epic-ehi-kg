# PR_EST_PREPAY_CMT

> Prepayment comment to be communicated to front-end staff when asking patient for required prepayment. This item is used when the estimate record is not linked to a patient contact.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the patient estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PR_EST_PREPAY_CMT` | VARCHAR |  | Stores a comment to go along with an entered prepayment amount. This is used when an estimate record is not linked to a patient contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

