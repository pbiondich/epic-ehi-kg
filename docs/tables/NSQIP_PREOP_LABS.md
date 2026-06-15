# NSQIP_PREOP_LABS

> The NSQIP_PREOP_LABS table contains information about preoperative lab data. This table is used in conjunction with NSQIP_INFO to provide NSQIP registry data for the surgeries that are selected for NSQIP submission.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NSQIP_LAB_COMPON_C_NAME` | VARCHAR |  | The category ID for the lab component. |
| 4 | `NSQIP_LAB_VALUE` | NUMERIC |  | The lab value. |
| 5 | `NSQIP_LAB_DT` | DATETIME |  | The date the lab was collected. |
| 6 | `NSQIP_LAB_UNKNOWN_YN` | VARCHAR |  | Indicates whether the lab component value is unknown. |
| 7 | `NSQIP_LAB_UNIT_C_NAME` | VARCHAR |  | The category ID of the NSQIP preop lab unit. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

