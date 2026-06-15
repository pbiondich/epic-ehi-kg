# HH_MED_EDIT_DETAILS

> This table stores details about medication edits in Home Health Remote Client.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HH_MED_EDIT_USER_ID` | VARCHAR |  | This item stores the user associated with the medication edit in the remote client. |
| 4 | `HH_MED_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `HH_MED_EDIT_INST_DTTM` | DATETIME (UTC) |  | This item stores the instant of the medication edit in the remote client. |
| 6 | `HH_MED_LVO_ID` | VARCHAR |  | This item stores the supplemental order ID (LVO) created for the medication edit in the remote client. |
| 7 | `HH_EDIT_EPISODE_ID` | NUMERIC |  | Tracks the Home Health/Hospice episode of the user who last edited/created the order (ORD) on the remote client. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

