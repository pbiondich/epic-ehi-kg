# MAMMO_HORMONES

> Mammography-relevant hormone history data.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HORMONE_C_NAME` | VARCHAR | org | The mammography hormones category ID for the order, documented by the tech in the visit navigator. |
| 4 | `START_DATE` | DATETIME |  | The date when the patient began taking the related hormone, documented by the tech in the visit navigator. |
| 5 | `END_DATE` | DATETIME |  | The date when the patient stopped taking the related hormone, documented by the tech in the visit navigator. |
| 6 | `COMMENT_NOTE_ID` | VARCHAR |  | The note ID for free-text information about the hormone history for this order. |
| 7 | `CURRENTLY_USING_YN` | VARCHAR |  | Indicates whether the patient with the order is currently using the hormone documented by the tech in the visit navigator. 'Y' indicates that the patient is using the hormone. 'N' or NULL indicates that the patient is not using the hormone. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

