# EMB_RSLT_TAGS

> Contains embryology specimen tags that were added on the result.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EMB_RSLT_EMB_SPEC_TAGS_C_NAME` | VARCHAR |  | Holds Embryology tags for the specimen that are added on the result. |
| 4 | `EMB_RSLT_EMB_SPEC_TAGS_C_CMT` | VARCHAR |  | A free-text comment related to one of a specimen's tags on the result. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

