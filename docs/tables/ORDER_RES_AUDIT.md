# ORDER_RES_AUDIT

> The table ORDER_RES_AUDIT stores audit data for result finding.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_DAT` | VARCHAR |  | This column stores a unique, internal contact date, in decimal format, when the audit action occurred for this result finding. |
| 4 | `AUDIT_ITEM` | VARCHAR |  | The result finding item that was modified in the audited action performed for this record. |
| 5 | `RES_AUDIT_USER_ID` | VARCHAR |  | This column stores the user who enacted the audit action for the items modified in this row. |
| 6 | `RES_AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `AUDIT_DTTM` | DATETIME (UTC) |  | This column records the instant at which the audit action was performed for this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

