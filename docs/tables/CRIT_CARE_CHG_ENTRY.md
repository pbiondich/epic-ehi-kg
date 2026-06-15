# CRIT_CARE_CHG_ENTRY

> This table stores the information for Critical Care Charging time entries. Time entries are duration-based incidents of critical care providers enter in Hyperspace.

**Primary key:** `INPATIENT_DATA_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the inpatient record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 4 | `CM_LOG_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| 5 | `ROW_ORDER_NUM` | INTEGER |  | Stores the order number for a patient's critical care charging time entry. |
| 6 | `ROW_DATE` | DATETIME |  | Stores the date for a patient's critical care charging time entry. |
| 7 | `ROW_SPECIALTY_C_NAME` | VARCHAR | org | Stores the provider specialty for a patient's critical care charging time entry. |
| 8 | `ROW_GRP` | VARCHAR |  | Stores the provider group for a patient's critical care charging time entry. |
| 9 | `ROW_IDENT_LN_NUM` | INTEGER |  | Stores the line of I INP 40000 of a patient's critical care charging identifier. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

