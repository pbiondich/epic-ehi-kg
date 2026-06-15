# OVERLAPPED_BED_DAY

> This table stores information at the claim service line level related to bed day types that overlap with the bed day types of the referral associated with the claim. To link this table’s service line information back to a claim header, join this table to AP_CLAIM_PROC_IDS on the TX_ID column. If you need to report on claim service lines specific to Cost Sharing Reduction (CSR), join this table instead to AP_CLAIM_PROC_IDS_CSR on the TX_ID column.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the AP Claim procedure transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OVRLP_BD_TYPE_ID` | NUMERIC |  | The unique identifier of the overlapped bed day type (TOD) from the referral linked to this procedure. |
| 4 | `OVRLP_BD_TYPE_ID_BED_DAY_TYPE_NAME` | VARCHAR |  | The name of the bed day type record (i.e. ICU or non-authorized.) |
| 5 | `OVRLP_BD_WGT` | NUMERIC |  | Stores the relative weight of this bed day type calculated against all bed day types on the matched referral that overlapped with the procedure's date range. |
| 6 | `OVRLP_BD_CONV_DAYS` | NUMERIC |  | Stores the converted bed days on the matched referral for the bed day types that overlap with the procedure's date range. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

