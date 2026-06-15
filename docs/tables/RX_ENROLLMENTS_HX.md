# RX_ENROLLMENTS_HX

> This table contains an audit trail history for edits made to a pharmacy enrollment.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RXENROLL_EDIT_USER_ID` | VARCHAR |  | The unique identifier for the user record who updated the pharmacy enrollment for a given edit. |
| 4 | `RXENROLL_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `RXENROLL_EDIT_DTTM` | DATETIME (Local) |  | The instant the pharmacy enrollment was updated on this edit |
| 6 | `ENROLL_PROG_C_NAME` | VARCHAR | org | The enrollment program category ID for the pharmacy enrollment on this edit |
| 7 | `RXENROLL_STATUS_C_NAME` | VARCHAR |  | The enrollment status category ID for this enrollment on this edit. |
| 8 | `RXENROLL_ENROLLMENT_DATE` | DATETIME |  | The enrollment start date documented for this enrollment on this edit |
| 9 | `RXENROLL_DISENROLL_DATE` | DATETIME |  | The disenrollment date documented on the enrollment on this edit |
| 10 | `RXENROLL_DECLINE_DATE` | DATETIME |  | The decline date documented on the enrollment on this edit |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

