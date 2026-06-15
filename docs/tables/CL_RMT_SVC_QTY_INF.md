# CL_RMT_SVC_QTY_INF

> This table contains the service line quantity information for a remittance record.

**Primary key:** `IMAGE_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | This is the ID for the remittance image record with related remit claim references. |
| 2 | `QTY_SVC_LN` | VARCHAR |  | This is the service line quantity information. |
| 3 | `SVC_QTY_QUAL_C_NAME` | VARCHAR |  | This is the service line level quantity qualifier. |
| 4 | `SVC_QTY` | NUMERIC |  | This is the service level quantity. |
| 5 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. (Standard for this column type) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

