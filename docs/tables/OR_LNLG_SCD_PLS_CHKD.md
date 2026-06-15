# OR_LNLG_SCD_PLS_CHKD

> This table contains documentation regarding where patient pulse is checked when sequential compression devices (SCD) are being used.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SCD_PULSE_CHECKED_C_NAME` | VARCHAR | org | This item is used to document where the patient's pulse was checked during or after a sequential compression device (SCD) application. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

