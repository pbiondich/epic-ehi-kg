# AN_STAFF_AUDIT

> This table contains the audit trail data for the anesthesia responsible staff activity. It contains a list of all the edits made to the information.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the Episode. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AN_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `AN_PROV_TYPE_C_NAME` | VARCHAR | org | The anesthesia staff type category number for the provider's responsible role. |
| 5 | `AN_BEGIN_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time when the provider began responsibility for the record. |
| 6 | `AN_END_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time when the provider ended responsibility for the record. |
| 7 | `AN_EDIT_USER_ID` | VARCHAR |  | The unique ID of the user who documented the responsible staff information. |
| 8 | `AN_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `AN_EDIT_DTTM` | DATETIME (UTC) |  | The date and time when the entry was modified. |
| 10 | `AN_EDIT_LN` | INTEGER |  | The line number from the anesthesia staff audit trail table that contains the previous information on this staff member's responsibility. |
| 11 | `AN_DELETED_YN` | VARCHAR |  | Indicates whether the responsible entry this value contains was deleted from the anesthesia staff table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

