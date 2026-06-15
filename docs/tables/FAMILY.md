# FAMILY

> The FAMILY table contains information about family records. A family is a group of patients that a user defines and that can subsequently share documentation.

**Primary key:** `FAMILY_ID`  
**Columns:** 3  
**Org-specific columns:** 1  
**Joined by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FAMILY_ID` | NUMERIC | PK | The unique identifier (.1 item) for the family record. |
| 2 | `FAMILY_TYPE_C_NAME` | VARCHAR | org | The family type category ID for the family. |
| 3 | `FAMILY_RECORD_TYPE_C_NAME` | VARCHAR |  | Determines the use case of the FMY record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (5)

| From | Column | Confidence |
|------|--------|------------|
| [FAMILY_PATS](FAMILY_PATS.md) | `FAMILY_ID` | high |
| [FAMILY_PATS_LINKED_EPSDS](FAMILY_PATS_LINKED_EPSDS.md) | `FAMILY_ID` | high |
| [FAMILY_PATS_STATUSES](FAMILY_PATS_STATUSES.md) | `FAMILY_ID` | high |
| [FAMILY_PATS_STATUS_DATES](FAMILY_PATS_STATUS_DATES.md) | `FAMILY_ID` | high |
| [PAT_REL_INFO_FAM](PAT_REL_INFO_FAM.md) | `FAMILY_ID` | high |

