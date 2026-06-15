# UC_GROUP

> This table contains information about Unified Communications groups.

**Primary key:** `UC_GROUP_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `UC_GROUP_ID_RECORD_NAME` | VARCHAR |  | Record name |
| 2 | `RECORD_NAME` | VARCHAR |  | Record name |
| 3 | `GROUP_DISPLAY_NAME` | VARCHAR |  | The name of the group, as it appears to end users. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [UC_GROUP_CONTACT](UC_GROUP_CONTACT.md) | `UC_GROUP_ID` | high |

