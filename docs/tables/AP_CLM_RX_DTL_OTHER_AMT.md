# AP_CLM_RX_DTL_OTHER_AMT

> This table contains information for other paid amounts for a single National Drug Code (NDC) code on a pharmacy claim.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OTHR_AMT_CODE_ID` | NUMERIC |  | Type of other paid amount. |
| 4 | `OTHR_AMT_CODE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 5 | `OTHR_AMT_PAID` | NUMERIC |  | Amount paid for additional costs. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

