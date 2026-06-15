# CL_RMT_CLM_ADJ

> This table contains the claim adjustment information from a remittance file. This information can be used to report claim level adjustments that cause the amount paid to differ from the amount originally charged.

**Primary key:** `IMAGE_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | The unique ID of the remittance image record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REASON_CODE` | VARCHAR |  | This is the code identifying the detailed reason the adjustment was made. |
| 4 | `ADJUST_AMT` | NUMERIC |  | This is the currency amount of the adjustment. |
| 5 | `ADJUST_QTY` | VARCHAR |  | The adjustment quantity. |
| 6 | `CLM_ADJ_CD_C_NAME` | VARCHAR | org | This is the code identifying the general category of payment adjustment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

