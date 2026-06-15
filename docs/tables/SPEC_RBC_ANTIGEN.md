# SPEC_RBC_ANTIGEN

> Contains information about red blood cell antigen testing.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 4 | `RBC_ANTIGEN_C_NAME` | VARCHAR |  | The RBC antigen category ID for the blood product specimen. |
| 5 | `RBC_LAB_ANTIGEN_RESULT_C_NAME` | VARCHAR |  | The RBC antigen testing result category ID for the blood product specimen. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

