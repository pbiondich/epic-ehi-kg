# ISLET_COLLAGN_TYPE

> Collagenase type and lot number for Islet organ.

**Primary key:** `ORG_RECORD_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORG_RECORD_ID` | NUMERIC | PK shared | The unique identifier for the organ record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COLLAGENASE_TYPE_C_NAME` | VARCHAR | org | Specify the collagenase type on islet testing |
| 4 | `LOT_NUM_COLLTYPE` | VARCHAR |  | Specify the lot number given for collagenase type |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

