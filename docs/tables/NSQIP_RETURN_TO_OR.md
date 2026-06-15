# NSQIP_RETURN_TO_OR

> The NSQIP_RETURN_TO_OR table contains return to OR information for NSQIP registry data for the surgeries that are selected for NSQIP submission. It is used in conjunction with the NSQIP_INFO table.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `REGISTRY_TYPE_C_NAME` | VARCHAR | org | The type of registry. |
| 3 | `CHILD_RECORD_NAME` | VARCHAR |  | The name for a child record. |
| 4 | `CHILD_RECORD_ABBR` | VARCHAR |  | The abbreviated name for a child record. |
| 5 | `NSQIP_RETURN_DATE` | DATETIME |  | The date the patient returned to the OR. |
| 6 | `NSQIP_RETURN_DATE_UNKNOWN_YN` | VARCHAR |  | Indicates if the date of an unplanned return to the OR is not known. |
| 7 | `NSQIP_RETURN_RELATED_C_NAME` | VARCHAR |  | Indicates if an unplanned return to the OR was related to the primary operative procedure. |
| 8 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status (hidden, soft-deleted, etc...) category ID for the registry data record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

