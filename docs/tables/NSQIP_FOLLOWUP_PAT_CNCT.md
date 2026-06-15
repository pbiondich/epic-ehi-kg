# NSQIP_FOLLOWUP_PAT_CNCT

> This table contains patient follow-up contact information for NSQIP registry data for the surgeries that are selected for NSQIP submission. It is used in conjunction with NSQIP_INFO table.

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
| 5 | `NSQIP_PAT_CONTACT_DATE` | DATETIME |  | The date of the follow-up patient contact. |
| 6 | `NSQIP_PAT_CONTACT_ACTION_C_NAME` | VARCHAR |  | The action taken for the follow-up patient contact. |
| 7 | `NSQIP_PAT_CONTACT_RESULT_C_NAME` | VARCHAR |  | The result of the follow-up patient contact. |
| 8 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status (hidden, soft-deleted, etc...) category ID for the registry data record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

