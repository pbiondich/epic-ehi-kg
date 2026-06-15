# CLAIM_INVOICE_STATUS_HX

> Stores the status change history for an AP claim invoice.

**Primary key:** `CLAIM_INVC_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_INVC_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the invoice record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHANGED_UTC_DTTM` | DATETIME (UTC) |  | Stores instant when status was changed in UTC time. |
| 4 | `PREV_INV_STAT_C_NAME` | VARCHAR |  | Stores the category identifier of the status the invoice was changed from. |
| 5 | `NEW_INV_STAT_C_NAME` | VARCHAR |  | Stores the category identifier of the status the invoice was changed to. |
| 6 | `CHANGE_COMMENT` | VARCHAR |  | Stores a comment related to the status change. |
| 7 | `CHANGED_DTTM` | DATETIME (Local) |  | Stores instant when status was changed in local time for the extracting deployment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_INVC_ID` | [CLAIM_INVOICE](CLAIM_INVOICE.md) | sole_pk | high |

