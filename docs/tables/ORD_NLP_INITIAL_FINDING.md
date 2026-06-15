# ORD_NLP_INITIAL_FINDING

> This table contains information about findings that were extracted from radiology reports by a natural language processing model.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FINDING_ID` | NUMERIC | shared | The unique ID of the finding record associated with this finding information. |
| 4 | `RSLT_TRK_FINDING_C_NAME` | VARCHAR | org | The finding category ID. |
| 5 | `ACUITY_LEVEL_C_NAME` | VARCHAR | org | The acuity category ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

