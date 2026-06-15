# CASE_FLAGS

> The CASE_FLAGS table holds the case flag information associated with the case records stored in the CASE_MGMT table. Each case record can have any number of flags assigned to it. This table stores every flag associated with each case record.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | NUMERIC | PK shared | The internal ID of the case record that this flag is associated with. |
| 2 | `LINE` | INTEGER | PK | The line number of the case flag that this row of information corresponds to. For instance, if the case has two flags, the first flag will have a Line value of 1 while the second will have a Line value of 2. |
| 3 | `FLAG_C_NAME` | VARCHAR | org | The category number associated with the flag assigned to the case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

