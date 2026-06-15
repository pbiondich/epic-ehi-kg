# ORGAN_RELATION

> The relationship between the transplant recipient and the transplant donor.

**Primary key:** `ORG_RECORD_ID`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORG_RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the organ record. |
| 2 | `TX_DNR_REL_C_NAME` | VARCHAR | org | Relation of donor to recipient |
| 3 | `SPEC_DONOR_REL` | VARCHAR |  | This item allows the user to specify a specific free-text donor relation when the DONOR RELATION (I ORG 315) category list is insufficient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

