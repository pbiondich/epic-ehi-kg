# EPI_ANTICOAG_PROV

> When the anticoagulation functionality is used, this table will contain the providers who initiated the enrollment for the patient. Ater the new functionalities added in 2010 version, the anticoag providers can be specified a role. The role can be obtained by joining the EPI_AC_PROV_INFO table, with the line number and summary block ID.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID of the episode of care record. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `INITIATING_SER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

