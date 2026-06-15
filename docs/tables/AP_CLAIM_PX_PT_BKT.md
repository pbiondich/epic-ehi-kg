# AP_CLAIM_PX_PT_BKT

> This table contains patient buckets involved with or affected by AP Claim service lines. To link this table’s service line information back to a claim header, join this table to AP_CLAIM_PROC_IDS on the TX_ID column. If you need to report on claim service lines specific to Cost Sharing Reduction (CSR), join this table instead to AP_CLAIM_PROC_IDS_CSR on the TX_ID column.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the AP Claim procedure transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BEN_BKT_COVERAGE_ID` | NUMERIC |  | The ID of the coverage associated with the benefit accumulation bucket that was involved in the adjudication of the procedure. |
| 4 | `BEN_BKT_ID` | NUMERIC |  | The ID of the benefit accumulation bucket that was involved in the adjudication of the procedure. |
| 5 | `BEN_BKT_ID_BUCKET_NAME` | VARCHAR |  | The name of the bucket. |
| 6 | `BEN_BKT_HX_LINE` | INTEGER |  | The benefit bucket accumulation history line number that corresponds to the state of the benefit bucket when it was used in the adjudication of the procedure. This column is often used to join to BEN_ACCUMULATION_HX_PAT.LINE. |
| 7 | `BEN_ACCUM_SEQUENCE_NUM` | INTEGER |  | The sequence number for the benefit accumulation associated with the procedure. |
| 8 | `BEN_ACCUM_PREV_TOTAL` | NUMERIC |  | The total of the benefit accumulation bucket before the benefit amounts were added for the procedure. |
| 9 | `BEN_BKT_LIMIT_TYPE_C` | VARCHAR |  | The limit type of the benefit accumulation bucket that was involved in the adjudication of the procedure. This is only populated for benefit accumulations where a benefit bucket is not specified. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

