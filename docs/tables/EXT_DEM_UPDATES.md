# EXT_DEM_UPDATES

> This table holds the systems and instants that updated demographics in Epic.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXT_DEM_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | This column holds the instant that the associated patient's demographics were updated from an external system (Data Exchange Organization). |
| 4 | `EXT_DEM_UPDATE_ORG_ID` | NUMERIC |  | This column holds the unique ID of the external system (Data Exchange Organization) from which we received the associated patient's demographic updates |
| 5 | `EXT_DEM_UPDATE_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

