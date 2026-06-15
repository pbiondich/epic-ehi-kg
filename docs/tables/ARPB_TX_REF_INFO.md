# ARPB_TX_REF_INFO

> This table stores additional information entered by users via the Refund Request Slip form.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RFND_ADDTL_INFO_FLD` | VARCHAR |  | This column contains the titles for additional fields in which users may enter additional information in the Refund Request Slip form. |
| 4 | `RFND_ADDTL_INFO_VAL` | VARCHAR |  | This column contains additional information entered by users in the Refund Request Slip form. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

