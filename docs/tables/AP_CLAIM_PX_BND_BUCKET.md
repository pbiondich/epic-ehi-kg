# AP_CLAIM_PX_BND_BUCKET

> Holds the bundle related information for a procedure.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BND_BUCKET_ID` | NUMERIC |  | Stores the bundle bucket IDs linked to the service. |
| 4 | `BND_BUCKET_ID_BUCKET_NAME` | VARCHAR |  | The name of the bucket. |
| 5 | `BND_BKT_AMT_ACCUM` | NUMERIC |  | Holds the amount the service currently contributes towards the bundle bucket. |
| 6 | `BND_BKT_QTY_ACCUM` | NUMERIC |  | Holds the quantity amount the service currently contributes towards the bundle bucket. |
| 7 | `BND_BKT_DTE_ACCUM_DATE` | DATETIME |  | Holds the service date that currently contributes towards the bundle bucket. |
| 8 | `BND_BKT_OVRIDE_AMT` | NUMERIC |  | Stores the amounts of the bundle bucket overrides. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

