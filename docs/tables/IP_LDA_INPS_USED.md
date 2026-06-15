# IP_LDA_INPS_USED

> This table stores the Inpatient Data (INP) records that have been charted upon for this LDA.

**Primary key:** `IP_LDA_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IP_LDA_ID` | VARCHAR | PK shared | Line/Drain/Airway ID |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INP_ID` | VARCHAR |  | This column stores the inpatient data (INP) records on which the LDA has been documented. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

