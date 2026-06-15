# PR_EST_PRO_SVC_TYPE_MULT

> Service type ID of the professional charge for all applicable coverages in the price estimate. This table has data for dental estimates using multiple coverages only. Refer to the PROC_SVC_TYPE_ID column in PR_EST_PROFEE_PROC for other dental estimates.

**Primary key:** `ESTIMATE_ID`, `PROC_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the patient estimate record. |
| 2 | `PROC_LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `PROC_SVC_TYPE_ID` | VARCHAR |  | The unique ID of the service type associated with the corresponding coverage (I PES 391). This is used to determine the benefits for the patient estimate. |
| 5 | `PROC_SVC_TYPE_ID_SERVICE_TYPE_NAME` | VARCHAR |  | The name of this benefit service type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

