# REHAB_RC_UTN_STATUS_AUDIT

> This table contains the audit information for the Review Choice Status item. This includes past values, users who changed the status, and when the status was changed.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REHAB_UTN_STATUS_C_NAME` | VARCHAR | org | This audit trail item stores past values of the Rehab - Review Choice UTN Status [I HSB 63034]. This is updated whenever the UTN status item is changed. |
| 4 | `REHAB_UTN_STAT_USER_ID` | VARCHAR |  | This audit trail item stores the user ID of the user who changed the value of the Rehab - Review Choice UTN Status [I HSB 63034]. This is updated whenever the UTN status item is changed. |
| 5 | `REHAB_UTN_STAT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `REHAB_UTN_STAT_UTC_DTTM` | DATETIME (UTC) |  | This audit trail item stores the instant users changed the value of the Rehab - Review Choice UTN Status [I HSB 63034]. This is updated whenever the UTN status item is changed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

