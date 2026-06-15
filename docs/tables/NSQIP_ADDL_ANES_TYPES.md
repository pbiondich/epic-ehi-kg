# NSQIP_ADDL_ANES_TYPES

> The NSQIP_ADDL_ANES_TYPES table contains information about additional anesthesia types associated with the surgery. This table is used in conjunction with NSQIP_INFO to provide NSQIP registry data for the surgeries that are selected for NSQIP submission.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NSQIP_ADDL_ANES_C_NAME` | VARCHAR |  | The category ID for the anesthesia technique administered outside of the principal anesthesia technique. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

