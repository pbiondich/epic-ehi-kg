# OR_LNLG_AN_EQP_CMT

> The OR_LNLG_AN_EQP_CMT table contains information about anesthesia equipment documented in surgical cases. The table stores comments data about the equipment being documented.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AN_EQUIP_COMMENTS` | VARCHAR |  | The comments entered about anesthesia equipment in intra-op. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

