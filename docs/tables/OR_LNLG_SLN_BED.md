# OR_LNLG_SLN_BED

> This table contains information on sentinel lymph node bed readings.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SENTINEL_LYMPH_NODE_BED` | VARCHAR |  | Which sentinel lymph node bed is being documented on |
| 4 | `SLN_BED_LOCATION_C_NAME` | VARCHAR | org | Where the sentinel lymph node bed is on the patient |
| 5 | `SLN_HOT_SPOT_READING` | NUMERIC |  | Reading of the sentinel lymph node bed hot spot |
| 6 | `SLN_BED_READING` | NUMERIC |  | Reading of the sentinel lymph node bed after incision |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

