# CL_RMT_REF_INFO

> This table contains the reference information from the remittance file when the receiver of the transaction is not the payee (e.g., Clearing House or billing service ID).

**Primary key:** `IMAGE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | This is the ID for the remittance image record. |
| 2 | `REF_ID_QUALIFIER_C_NAME` | VARCHAR |  | Code qualifying the Reference Identification |
| 3 | `REFERENCE_INFO` | VARCHAR |  | Reference information as defined for a particular Transaction Set or as specified by the Reference Identification Qualifier |
| 4 | `LINE` | INTEGER | PK | The line number in the results of a query. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

