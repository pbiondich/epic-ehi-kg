# REG_DEMOGRAPHIC_CHANGE

> Contains information about updates to patient demographic info.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REG_DEM_CHNG_INST_DTTM` | DATETIME (UTC) |  | Stores the UTC instant that an audited demographic item was changed. |
| 4 | `REG_DEM_CHNG_ITEM` | INTEGER |  | Stores the source demographic item when that item's value changes. Used for auditing purposes. |
| 5 | `REG_DEM_CHNG_USER_ID` | VARCHAR |  | Stores the unique ID of the user who is responsible for changing the value of an audited demographic item. |
| 6 | `REG_DEM_CHNG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

