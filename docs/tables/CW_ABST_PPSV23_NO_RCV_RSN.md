# CW_ABST_PPSV23_NO_RCV_RSN

> No documentation reasons for PPSV23 from abstractions with clinical information reported to the United States ESRD patient registry.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PPSV23_NOT_RECV_RSN_C_NAME` | VARCHAR | org | The reason why the dialysis patient's PPSV23 pneumococcal vaccination administration was not documented. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

