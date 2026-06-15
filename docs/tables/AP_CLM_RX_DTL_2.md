# AP_CLM_RX_DTL_2

> This table contains information for a single NDC code on a pharmacy claim.

**Overflow of:** [AP_CLM_RX_DTL](AP_CLM_RX_DTL.md)  
**Primary key:** `TX_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record |
| 2 | `HAS_UNMAPPED_CODE_YN` | VARCHAR |  | Indicates whether a service line has an unmapped NDC code. 'Y' indicates that the service line has unmapped NDC code. 'N' or NULL indicates that the service line is linked to an NDC code. |
| 3 | `DTL_SVC_CLASS_C_NAME` | VARCHAR |  | Represents a detailed clinical classification of the billed service. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

