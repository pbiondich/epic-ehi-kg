# OPE_CASELOG_ADDL_INFO

> The OPE_CASELOG_ADDL_INFO table is an extension of the OR management system log procedures (OR_LOG_ALL_PROC) table. It contains additional information about log procedures.

**Primary key:** `OPE_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OPE_ID` | NUMERIC | PK shared | The unique identifier for the orders performed record. |
| 2 | `CASELOG_DATATYPE_C_NAME` | VARCHAR |  | Determines if this is a case or log procedure additional data record. |
| 3 | `CASELOG_LOG_ID` | VARCHAR |  | The log record ID when the procedure additional data item is for a log. |
| 4 | `CASELOG_PROC_DATE` | DATETIME |  | The date of the procedure. |
| 5 | `CASELOG_CASE_ID` | VARCHAR |  | The case record ID when the procedure additional data item is for a case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

