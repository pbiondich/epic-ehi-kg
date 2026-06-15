# CRIT_CARE_CHG_ENTRY_MOD

> This table stores the information for Critical Care Charging modifiers on time entries. Time entries are duration-based incidents of critical care providers enter in Hyperspace.

**Primary key:** `INPATIENT_DATA_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the inpatient record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 5 | `CM_LOG_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| 6 | `ROW_MODIFIER_ID` | VARCHAR |  | Stores the lists of modifiers for a patient's critical care charging time entry. |
| 7 | `ROW_MODIFIER_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

