# OR_PKLST

> The OR_PKLST table contains OR management system pick lists.

**Primary key:** `PICK_LIST_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PICK_LIST_ID` | VARCHAR | PK | The unique internal ID of the pick list record. |
| 2 | `PICK_LIST_NAME` | VARCHAR |  | The name of the pick list record. |
| 3 | `LOG_ID` | VARCHAR | shared | The unique ID of the log record associated with this pick list record. This is the value derived from PCK item 40 to define an explicit network link to the log ID (ORL) and is only defined if the log exists . |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [OR_PKLST_SUP_LIST](OR_PKLST_SUP_LIST.md) | `PICK_LIST_ID` | high |

