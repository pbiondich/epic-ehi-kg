# REI_RES_GENETIC_CONTRIBS

> Information about the genetic contributors for the associated result for an embryology procedure.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EMB_RSLT_GC_RECORD_ID` | NUMERIC |  | Stores the RQG patients who are a genetic contributor for an embryology procedure |
| 4 | `EMB_RSLT_GENTYPE_C_NAME` | VARCHAR | org | Stores the genetic contribution type for a patient during an embryology procedure |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

