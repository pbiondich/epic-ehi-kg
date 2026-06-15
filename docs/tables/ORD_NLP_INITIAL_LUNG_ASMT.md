# ORD_NLP_INITIAL_LUNG_ASMT

> This table contains information about lung screening assessments that were extracted from radiology reports by a natural language processing model.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SX_PROG_ASMT_C_NAME` | VARCHAR |  | The screening program assessment category ID. |
| 4 | `MODIFIER_SX_PROG_ASMT_C_NAME` | VARCHAR |  | The screening program assessment modifier category ID. |
| 5 | `INCOMPLETE_RSN_SX_PROG_ASMT_C_NAME` | VARCHAR |  | The screening program assessment incomplete reason category ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

