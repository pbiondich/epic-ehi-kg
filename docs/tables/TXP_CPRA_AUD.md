# TXP_CPRA_AUD

> The audit trail for the calculated panel reactive antibody (CPRA) score of a patient.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CPRA_AUDIT` | INTEGER |  | Calculated Panel Reactive Antibodies (CPRA) value for entry in audit trail. |
| 4 | `CPRA_DATE_AUDIT_DT` | DATETIME |  | Effective date for corresponding Calculated Panel Reactive Antibodies (CPRA) in audit trail. |
| 5 | `CPRA_UPDATE_USER_ID` | VARCHAR |  | The updating user for the corresponding audit trail entry. |
| 6 | `CPRA_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `CPRA_UPDATE_INSTANT_DTTM` | DATETIME (UTC) |  | The instant the corresponding audit trail entry occurred. |
| 8 | `CPRA_AUDIT_EVENT_C_NAME` | VARCHAR |  | The type of audit event that occurred. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

