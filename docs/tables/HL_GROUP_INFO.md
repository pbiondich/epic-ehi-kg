# HL_GROUP_INFO

> Hospital Logistics Group Information.

**Primary key:** `HLR_ID`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLR_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the request record. |
| 2 | `HLR_TYPE_C_NAME` | VARCHAR |  | The Hospital Logistics Request type. |
| 3 | `GROUP_TYPE_C_NAME` | VARCHAR | org | Indicates what type of Logistics Group this is. |
| 4 | `GROUP_STATUS_C_NAME` | VARCHAR |  | This Logistics Group's current status. |
| 5 | `GROUP_REGION_SEC_ID` | NUMERIC |  | The Logistics Region that this Group belongs to. |
| 6 | `GROUP_REGION_SEC_ID_RECORD_NAME` | VARCHAR |  | The name of this cleaning sector. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

