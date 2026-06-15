# HH_EPSD_WOUND_LIST

> This table contains the system-generated wound IDs for the user-entered wounds for Home Health episodes. These wounds are entered during encounters documented on the Home Health Remote Client. This table contains only the Wounds IDs for the episode. The rest of the wound information can be found in tables HH_PBLST_INFO and HH_PBLST_WOUNDS.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `WOUND_LIST_ID` | NUMERIC |  | ID for the wound on the list. Links to table HH_PBLST_INFO. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

