# AN_DELETION_AUDIT

> This table contains the audit trail data for deleted anesthesia records.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DELETION_USER_ID` | VARCHAR |  | Audit item that stores the ID of the user who deleted the anesthesia record. |
| 4 | `DELETION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `DELETION_UTC_DTTM` | DATETIME (UTC) |  | Audit item that stores the instant that the anesthesia record was deleted. |
| 6 | `AN_DEL_TYPE_C_NAME` | VARCHAR |  | Audit item for whether the anesthesia record was hard- or soft-deleted. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

