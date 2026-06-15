# PR_EST_PRO_SYS_ALLOW_MULT

> System-calculated allowed amount for all applicable coverages for the professional charge in the price estimate. This table has data for dental estimates using multiple coverages only. Refer to the SYS_ALLOWED_AMT column in PR_EST_PROFEE_PROC for all other cases.

**Primary key:** `ESTIMATE_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the patient estimate record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `PROC_MUL_SYSALL_AMT` | NUMERIC |  | The system-calculated allowed amount for the procedure and corresponding coverage (I PES 168). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

