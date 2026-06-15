# FINDING_TEXT_GEN_SUMMARY

> This table contains the generated summary text that is associated with a particular finding.

**Primary key:** `FINDING_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the generated summary text information associated with this finding. Together with FINDING_ID, this forms the foreign key to the FINDING_TEXT_GEN table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple generated summary text values associated with the finding and the item from the FINDING_TEXT_GEN table. |
| 4 | `SUMMARY_TEXT` | VARCHAR |  | The generated summary text that is associated with a particular finding. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

