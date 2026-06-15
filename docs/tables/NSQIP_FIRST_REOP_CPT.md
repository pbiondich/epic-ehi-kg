# NSQIP_FIRST_REOP_CPT

> This table contains CPT® and procedure description related to the first reoperation.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NSQIP_FST_REOP_INF_SRC_C_NAME` | VARCHAR |  | The category ID for the source of information for the first return to the OR. |
| 4 | `NSQIP_FST_REOP_CPT` | VARCHAR |  | CPT® code associated with the first return to the OR. |
| 5 | `NSQIP_FST_REOP_PROC_DESC` | VARCHAR |  | Procedure description associated with the first return to the OR. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

