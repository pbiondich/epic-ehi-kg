# OR_CASE_CHARGING_PROCS

> This table contains information about procedures grouped for charging flags.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHARGE_PROC_ID` | VARCHAR |  | The procedures grouped for charging flags. This does not drive charging automatically, but is informational. |
| 4 | `CHARGE_PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 5 | `CHARGE_COSMETIC_C_NAME` | VARCHAR | org | Whether the procedure is cosmetic. This does not drive charging automatically, but is informational. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

