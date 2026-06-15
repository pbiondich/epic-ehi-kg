# ORGAN_EXTRA_VESSEL

> Extra vessels used during transplant.

**Primary key:** `ORG_RECORD_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORG_RECORD_ID` | NUMERIC | PK shared | The unique identifier for the organ record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VESSEL_DUID` | VARCHAR |  | Donor ID from the United Network for Organ Sharing (UNOS) of the extra vessel used in the transplant. |
| 4 | `VESSEL_PLACEMENT_C_NAME` | VARCHAR | org | The location of any extra vessels used during transplant. |
| 5 | `VESSEL_COMMENTS` | VARCHAR |  | Any comments about the donor vessels used during transplant. |
| 6 | `VESSEL_TYPE_C_NAME` | VARCHAR | org | The type of donor vessels used during transplant. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

