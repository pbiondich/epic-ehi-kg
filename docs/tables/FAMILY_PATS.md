# FAMILY_PATS

> The FAMILY_PATS table stores the list of patients included in a family. It includes active family members in addition to family members who were previously deleted or marked as historic.

**Primary key:** `FAMILY_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FAMILY_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the family record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient who is a member of the family. |
| 4 | `FAMILY_ROLE_C_NAME` | VARCHAR | org | The family role category ID for the family member. |
| 5 | `PRIMARY_HOUSEHOLD_YN` | VARCHAR |  | Indicates whether the family member is part of the primary household for this family. 'Y' indicates that they are a primary household member. 'N' indicates that they are not. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FAMILY_ID` | [FAMILY](FAMILY.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

