# CLP_EOB_PAID_LINE

> This table holds the service line level secondary information for a non-primary claim. It contains the paid amount and other secondary amounts other than claim adjustments (CAS).

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 3 | `EOB_LN_CVG_ID` | NUMERIC |  | This item holds the line level coverage ID associated with American National Standards Institute secondary information that does not span multiple lines. |
| 4 | `EOB_LN_CLM_LN` | INTEGER |  | The line number of one of the multiple values associated with a specific group of data within this record. |
| 5 | `EOB_LN_PAID` | NUMERIC |  | This item holds the line level paid amount for American National Standards Institute secondary claims. |
| 6 | `EOB_LN_CONTRACT` | NUMERIC |  | This item holds the line level contract amount for American National Standards Institute secondary claims. |
| 7 | `EOB_LN_DATE` | DATETIME |  | This item holds the line level adjudication date for American National Standards Institute secondary claims. |
| 8 | `EOB_LN_REMIT_IMAGE_ID` | VARCHAR |  | For ANSI secondaries this item may hold a line level matched remittance image (IMD) record ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

