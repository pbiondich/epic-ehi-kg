# CAL_COMM_HX_REF_PAT_REL

> Stores the history of source relationships to patients referenced by a communication (i.e. the history of CAL_REFERENCE_PAT.REF_PAT_REL_C). Each GROUP_LINE corresponds to a line in CAL_COMM_HX for a COMM_ID.

**Primary key:** `COMM_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | VARCHAR | PK shared | The unique identifier for the communication record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `HX_REF_PAT_REL_C_NAME` | VARCHAR | org | Stores the category identifier of the relationship a source has to the patient referenced (CAL_COMM_HX_REF_PAT). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

