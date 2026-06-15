# RECONCILE_SVC_CTDT

> This table contains raw line-level category codes received through claims reconciliation. This information is only populated if the line-level category code was not mapped to an Epic category value.

**Primary key:** `CLAIM_RECON_ID`, `CONTACT_DATE_REAL`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_RECON_ID` | VARCHAR | PK | The unique ID of the claim reconciliation record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this contact in your system. The integer portion of the number specifies the date of the contact. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 4 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this contact. |
| 5 | `CONTACT_DATE` | DATETIME |  | The contact date of the record, in external format. |
| 6 | `LN_CATEGORY_DATA` | VARCHAR |  | Line-level category code (raw data). This value is only populated if the line-level category code was not mapped to a category value from inside the system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

