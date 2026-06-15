# BI_VERSIONED_OUTCOMES

> This table contains information about the Breast Imaging outcomes. This includes the outcome version, the final outcome, and the preliminary outcome. The rows in this table are order (ORD) records that are exams with a breast imaging outcome.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BI_OUTCOME_VER_C_NAME` | VARCHAR |  | The version of MQSA outcomes that are being calculated. |
| 4 | `BI_VER_MAMMO_OUTCOME_C_NAME` | VARCHAR |  | Stores versioned FP/FN/TP/TN/etc info for a mammo study. May not contain the most current data until the MQSA report has been run. |
| 5 | `BI_VER_PRELIM_MAMMO_OUTCOME_C_NAME` | VARCHAR |  | Stores versioned preliminary FP/FN/TP/TN/etc. info for a breast imaging study. May not contain the most current data until the MQSA report has been run. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

