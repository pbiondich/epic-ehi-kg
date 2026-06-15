# ST_FINDING_DETAILS

> This table shows the details of a soft tissue finding.

**Primary key:** `FINDING_ID`, `CONTACT_DATE_REAL`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `ST_FIND_TYPE_C_NAME` | VARCHAR |  | The soft tissue finding type, documenting severity of the finding. |
| 5 | `ST_AVAT_TYPE_C_NAME` | VARCHAR |  | The soft tissue avatar type, which is either extraoral or intraoral. |
| 6 | `ST_FIND_STATUS_C_NAME` | VARCHAR |  | The current status of the soft tissue finding, which is either unresolved, resolved, or removed. |
| 7 | `ST_MOD_USER_ID` | VARCHAR |  | A unique user identifier that consists of the name and the user ID of the user that modified the soft tissue finding. |
| 8 | `ST_MOD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `ST_MOD_INST_DTTM` | DATETIME (UTC) |  | The instant when the soft tissue finding was modified. |
| 10 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 11 | `REGION_RECORD_ID` | NUMERIC |  | The unique ID of the anatomy region associated with the soft tissue finding. |
| 12 | `REGION_RECORD_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 13 | `FINDING_COUNT` | INTEGER |  | The number of findings this soft tissue finding represents. Allows user to document like findings in the same region under one soft tissue finding record. |
| 14 | `FINDING_LOC_NAME` | VARCHAR |  | The display name of the soft tissue finding that overrides the finding's default name of the associated anatomy region. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

