# IP_HANDOFF

> The table contains information of a handoff field.

**Primary key:** `HANDOFF_ID`  
**Columns:** 6  
**Org-specific columns:** 2  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HANDOFF_ID` | NUMERIC | PK | The unique identifier (.1 item) for the handoff data record. |
| 2 | `PAT_CSN_ID` | NUMERIC |  | The contact serial number (CSN) of the patient contact on which the Handoff was written. |
| 3 | `SERVICE_C_NAME` | VARCHAR | org | The service of the handoff field. |
| 4 | `PURPOSE_C_NAME` | VARCHAR | org | This item defines the purpose of the handoff field. |
| 5 | `INSTANT_OF_UPDATE_DTTM` | DATETIME (Local) |  | This item stores the instant the record was last locked/unlocked. |
| 6 | `PREVIOUS_HANDOFF_ID` | NUMERIC |  | When Handoff is edited 100+ times in a day, a new SOD record is created, and this item is used to link back to the original/previous SOD record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [HANDOFF_EDIT_TEXT](HANDOFF_EDIT_TEXT.md) | `HANDOFF_ID` | high |
| [HANDOFF_TASK_LIST](HANDOFF_TASK_LIST.md) | `HANDOFF_ID` | high |
| [IP_HANDOFF_INFO](IP_HANDOFF_INFO.md) | `HANDOFF_ID` | high |

