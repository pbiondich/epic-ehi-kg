# DENTAL_REFERRAL_HX

> The DENTAL_REFERRAL_HX table contains the audit history of the dental referral status (Referred, Completed, Removed) of a specified dental referral order over time, also noting the encounter and timestamp of the change.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DENTAL_REFERRAL_DAT` | VARCHAR |  | This item stores the patient encounter DAT in which the dental order associated with a referral was modified. |
| 4 | `DENTAL_RFL_MOD_INST_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant when the status of an order associated with a dental referral was modified. |
| 5 | `DENT_REFERRAL_STATUS_HX_C_NAME` | VARCHAR |  | This item keeps track of how the status of a dental referral changes over time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

