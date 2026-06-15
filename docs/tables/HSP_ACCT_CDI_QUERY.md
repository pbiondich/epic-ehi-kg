# HSP_ACCT_CDI_QUERY

> This table stores the queries sent to physicians as part of the Clinical Documentation Improvement (CDI) process.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the hospital account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CDI_QUERY_TYPE_C_NAME` | VARCHAR | org | Stores the type of the query sent to the provider. |
| 4 | `CDI_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `CDI_QUERY_RESP_YN` | VARCHAR |  | Indicates whether a response was received from the provider for the clinical documentation improvement (CDI) query. |
| 6 | `CDI_DRG_CHNG_RSN_C_NAME` | VARCHAR | org | Stores the reason for the DRG change caused by the query. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

