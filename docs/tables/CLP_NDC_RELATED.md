# CLP_NDC_RELATED

> This table holds the National Drug Code (NDC) information on the claim.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | This is the claim record ID. |
| 2 | `LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 3 | `NDC_CODE_ID` | VARCHAR |  | This is the National Drug Code ID. |
| 4 | `NDC_CODE_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 5 | `NDC_NUMBER` | VARCHAR |  | This is the National Drug Code number. |
| 6 | `NDC_QTY` | NUMERIC |  | This is the National Drug Code quantity. |
| 7 | `NDC_UNITS_C_NAME` | VARCHAR |  | This holds the units of the drug. The units are billing appropriate. |
| 8 | `CLAIM_LINE_PTR` | NUMERIC |  | This field points to a claim line. |
| 9 | `ERX_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 10 | `RX_NUM` | VARCHAR |  | This holds the prescription number. |
| 11 | `COMPOUND_LINK_NUM` | VARCHAR |  | This holds the Link Sequence Number used to associate ingredients of a compound drug. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

