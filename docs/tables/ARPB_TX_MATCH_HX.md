# ARPB_TX_MATCH_HX

> Matching History Transaction Related Items. A line is added to this related group whenever two transactions are matched together.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MTCH_TX_HX_DT` | DATETIME |  | This item stores the date that a transaction was matched to this transaction. |
| 4 | `MTCH_TX_HX_ID` | NUMERIC |  | This item stores the transaction that this transaction was matched to. If the MTCH_TX_HX_UN_DT is null, then the transaction is still currently matched to this transaction. |
| 5 | `MTCH_TX_HX_AMT` | NUMERIC |  | This item stores the (insurance+self-pay) amount for which this transaction is matched to the transaction in column MTCH_TX_HX_ID. |
| 6 | `MTCH_TX_HX_INS_AMT` | NUMERIC |  | This item stores the insurance amount for which this transaction is matched to the transaction in column MTCH_TX_HX_ID. |
| 7 | `MTCH_TX_HX_PAT_AMT` | NUMERIC |  | This item stores the self-pay amount for which this transaction is matched to the transaction in column MTCH_TX_HX_ID. |
| 8 | `MTCH_TX_HX_COMMENT` | VARCHAR |  | This item holds the comment for the matching of this transaction to the transaction in column MTCH_TX_HX_ID. This item is typically only populated by the system and not user entered comments. |
| 9 | `MTCH_TX_HX_UN_DT` | DATETIME |  | This item holds the date that the transaction was unmatched from the transaction in column MTCH_TX_HX_ID. |
| 10 | `MTCH_TX_HX_D_CVG_ID` | NUMERIC |  | This item stores the coverage ID at the time that the transaction was matched to the transaction in column MTCH_TX_HX_ID. |
| 11 | `MTCH_TX_HX_DSUSR_ID` | VARCHAR |  | This item stores the users who matched this transaction to the transaction from column MTCH_TX_HX_ID. |
| 12 | `MTCH_TX_HX_DSUSR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `MTCH_TX_HX_UDUSR_ID` | VARCHAR |  | This item stores the user that unmatched this transaction from the transaction in the MTCH_TX_HX_ID column. |
| 14 | `MTCH_TX_HX_UDUSR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `MTCH_TX_HX_INV_NUM` | VARCHAR |  | This item stores the invoice associated with the debit transaction in the matching group. |
| 16 | `MTCH_TX_HX_UN_COM` | VARCHAR |  | This item stores the comment entered when the transaction is undistributed. |
| 17 | `MTCH_TX_HX_UN_CV_ID` | NUMERIC |  | This is the coverage of the debit transaction at the time of unmatch. |
| 18 | `MTCH_TX_HX_LINE` | INTEGER |  | This item stores the corresponding line from the matched transaction. |
| 19 | `MTCH_TX_HX_DTTM` | DATETIME (UTC) |  | The UTC date and time the transaction was matched. |
| 20 | `MTCH_TX_HX_UN_DTTM` | DATETIME (UTC) |  | The UTC date and time the transaction was unmatched. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

