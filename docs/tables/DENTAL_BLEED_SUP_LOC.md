# DENTAL_BLEED_SUP_LOC

> This table contains the location of bleeding and suppuration findings documented during a patient's periodontal exam.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DENT_BL_SUP_LOC_C_NAME` | VARCHAR | org | Stores the physical location where bleeding or suppuration findings were noted. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

