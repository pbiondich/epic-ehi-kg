# ATTRIBUTED_PROV_GROUP

> This table contains information about Attributed Provider Group (APG) records.

**Primary key:** `ATTRIBUTED_GROUP_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ATTRIBUTED_GROUP_ID` | NUMERIC | PK | The unique identifier (.1 item) for the subject name record. |
| 2 | `ATTRIBUTED_GROUP_ID_PROV_GROUP_NAME` | VARCHAR |  | Record name |
| 3 | `PROV_GROUP_NAME` | VARCHAR |  | Record name |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [MPM_ATTRIB_PROV](MPM_ATTRIB_PROV.md) | `ATTRIBUTED_GROUP_ID` | high |

