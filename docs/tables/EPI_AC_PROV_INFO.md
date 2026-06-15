# EPI_AC_PROV_INFO

> This table stores external providers of the anticoagulation episode. It can also be used for internal providers. To match the role of an internal provider, a join has to be made to the EPI_ANTICOAG_PROV table using columns SUMMARY_BLOCK_ID and LINE.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ANTICOAG_PROV_NAME` | VARCHAR |  | Anticoagulation freetext provider(s) |
| 4 | `ANTICOAG_PRO_ROLE_C_NAME` | VARCHAR | org | Anticoag provider(s) role |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

