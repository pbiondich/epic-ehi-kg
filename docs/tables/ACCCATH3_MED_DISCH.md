# ACCCATH3_MED_DISCH

> ACC-NCDR CathPCI Registry v3 Medications - Discharge table. This main columns of this table includes the information related to the discharge medication that was administered, not administered, contraindicated or blinded. In addition to that, there are few other columns which contains data (owner etc) related to each record of this table.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The registry data ID for this record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DISCHRG_MED_C_NAME` | VARCHAR | org | Indicate the ACC assigned ID for the discharge medication. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

