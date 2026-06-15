# MEM_LIST_ACCUM_INFO

> Tier accumulation information for this member list.

**Primary key:** `MEM_LIST_ID`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MEM_LIST_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the member list record. |
| 2 | `ACCUM_BROKERAGE_ID` | VARCHAR |  | The brokerage for which the members in this list are tiered. |
| 3 | `ACCUM_BROKERAGE_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |
| 4 | `ACCUM_PLAN_GRP_ID` | VARCHAR |  | The employer group for which the members in this list are tiered. |
| 5 | `ACCUM_PLAN_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |
| 6 | `ACCUM_CORP_ID` | VARCHAR |  | The corporation for which members in this list are tiered. |
| 7 | `ACCUM_CORP_ID_CORP_NAME` | VARCHAR |  | The name of the corporation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

