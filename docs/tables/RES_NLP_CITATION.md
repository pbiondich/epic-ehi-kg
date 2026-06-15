# RES_NLP_CITATION

> Contains citation information used by the NLP model when creating RES records.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CITATION` | VARCHAR |  | Holds citation information used by the model when generating the recommendations and follow ups. |
| 4 | `START_IDX` | INTEGER |  | Character index of the start of an AI-provided citation in the result text. |
| 5 | `END_IDX` | INTEGER |  | Character index of the end of an AI-provided citation in the result text. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

