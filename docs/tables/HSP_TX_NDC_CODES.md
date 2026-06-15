# HSP_TX_NDC_CODES

> Table for National Drug Code (NDC) codes and related information.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `NDC_CODE_RG_ID` | VARCHAR |  | Holds medication national drug codes associated with the charge. |
| 4 | `NDC_CODE_RG_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 5 | `NDC_CODE_ADMIN_AMT` | NUMERIC |  | Administered amount for associated national drug code. |
| 6 | `NDC_CODE_UNIT_C_NAME` | VARCHAR |  | This column stores the unit associated with National Drug Code administered amount for the hospital billing transaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

