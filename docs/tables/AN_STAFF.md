# AN_STAFF

> This table contains information about the providers who have been documented as being responsible on an anesthesia record, including their role and begin and end times.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the Episode. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AN_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `AN_PROV_TYPE_C_NAME` | VARCHAR | org | The anesthesia staff type category number for the provider's responsible role. |
| 5 | `AN_BEGIN_LOCAL_DTTM` | DATETIME (Local) |  | The local date and time when the provider began responsibility for the record. |
| 6 | `AN_BEGIN_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time when the provider began responsibility for the record. |
| 7 | `AN_END_LOCAL_DTTM` | DATETIME (Local) |  | The local date and time when the provider ended responsibility for the record. |
| 8 | `AN_END_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time when the provider ended responsibility for the record. |
| 9 | `AN_EDIT_USER_ID` | VARCHAR |  | The unique ID of the user who documented the responsible staff information. |
| 10 | `AN_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `AN_EDIT_DTTM` | DATETIME (UTC) |  | The date and time when the entry was modified. |
| 12 | `AN_EDIT_LN` | INTEGER |  | The line number from the anesthesia staff audit trail table that contains the previous information on this staff member's responsibility. |
| 13 | `AN_BEGIN_PAT_DTTM` | DATETIME (Local) |  | Contains the start time of the staff member. The time is in the patient department's time zone. |
| 14 | `AN_END_PAT_DTTM` | DATETIME (Local) |  | Contains the end time of the staff member. The time is in the patient department's time zone. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

