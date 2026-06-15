# OR_CASE_RTF_INSTR

> This table contains the case instructions information for the surgical case (ORC) record.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique ID of the procedural case record. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `INSTRUCTION_TYPE_C_NAME` | VARCHAR | org | The type of instructions on this line. |
| 4 | `INSTRUCTION_ID` | VARCHAR |  | The ID of the instructions HNO record. |
| 5 | `INSTRXNS_EDITED_YN` | VARCHAR |  | Has the instructions record on this line been edited since it was last built? |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

