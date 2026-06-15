# BIL_PROV_CNCT

> All values associated with a claim are stored in the Claim External Value record. The BIL_PROV_CNCT table holds contact information for the billing provider on the claim.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `BIL_PROV_CNCT_QUAL` | VARCHAR |  | This item holds a qualifier describing contact information (phone number, email, etc) for the billing provider. |
| 4 | `BIL_PROV_CNCT_INFO` | VARCHAR |  | This item holds contact information (phone number, email, etc) for the billing provider. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

