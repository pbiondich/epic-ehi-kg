# ARPB_PMT_RELATED_DENIALS

> Denial records associated with this payment for evaluating denial rate metrics.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RELATED_BDC_ID` | NUMERIC |  | Returns denial records associated with this payment for purposes of denial rate calculations. Denials with a 18-Duplicate Claim/Service remittance reason are not included in denial rate metrics. Only denials that have been converted to the Denial/Remark/Correspondence framework are included here. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

