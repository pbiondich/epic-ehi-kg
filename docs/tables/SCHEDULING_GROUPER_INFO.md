# SCHEDULING_GROUPER_INFO

> This table includes information about your scheduling grouper records. This includes information about record status and override record information.

**Primary key:** `GROUPER_ID`  
**Columns:** 4  
**Joined by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 2 | `OVERRDE_STATUS_C_NAME` | VARCHAR |  | Stores the override record status |
| 3 | `OVERRIDE_CONTEXT` | VARCHAR |  | Stores the override context for the record |
| 4 | `PARENT_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (5)

| From | Column | Confidence |
|------|--------|------------|
| [ACCT_GUAR_GROUPER](ACCT_GUAR_GROUPER.md) | `GROUPER_ID` | high |
| [V_EHI_LNO_LINKED_RQGS](V_EHI_LNO_LINKED_RQGS.md) | `GROUPER_ID` | high |
| [V_EHI_NCS_FILTER_RQG](V_EHI_NCS_FILTER_RQG.md) | `GROUPER_ID` | high |
| [V_EHI_ORD_LINKED_RQGS](V_EHI_ORD_LINKED_RQGS.md) | `GROUPER_ID` | high |
| [V_EHI_OVR_LINKED_RQGS](V_EHI_OVR_LINKED_RQGS.md) | `GROUPER_ID` | high |

