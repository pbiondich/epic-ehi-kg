# CLM_ADJ_RSN_CD

> This table holds the claim adjustment reason code information for the claim. Each record holds the set of reason codes and amounts for one coverage at either the claim or service line level.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the Claim Info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `CAS_GRP_CD` | VARCHAR |  | This item holds the group code for a claim adjustment reason code. Group codes from both claim level and line level adjustments will be stored in this item. |
| 4 | `CAS_RSN_CD` | VARCHAR |  | This item holds a claim adjustment reason code. Both claim level and line level reason codes will be stored in this item. |
| 5 | `CAS_AMT` | NUMERIC |  | This item holds the amount for a claim adjustment reason code. Amounts from both claim level and line level adjustments will be stored in this item. |
| 6 | `CAS_QTY` | NUMERIC |  | This item holds the quantity for a claim adjustment reason code. Quantities from both claim level and line level adjustments will be stored in this item. |
| 7 | `BB_AMT_TYPE` | VARCHAR |  | The Uniform Resource Identifier (URI) provided by the Beneficiary Claims Data API (BCDA), for determining the adjudication amount type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

