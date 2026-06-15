# LAB_RSLT_TST_AGAINST_GRP

> This table contains information about additional context in which groups of components on a result were performed. Each row represents a unique combination of contextual information by which components on a result should be grouped.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TST_AGAINST_GRP_NAM` | VARCHAR |  | Name or key for the most important contextual information for a result (e.g. a blood product or a particular container from the specimen which was involved in testing), indicating that all rows with this value for a result should be logically grouped together. |
| 4 | `TST_GRP_DON_SPECIMEN_ID` | VARCHAR |  | Pointer to a specimen record that a group of components was tested against. Specimen records in this item should not be treated like normal specimens collected from a patient, as they may be some kind of non-patient specimen, like blood products, and have special considerations. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

