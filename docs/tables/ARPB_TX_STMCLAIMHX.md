# ARPB_TX_STMCLAIMHX

> This table contains information about the statement and claim history for professional billing transactions.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the transaction record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `BC_HX_TYPE_C_NAME` | VARCHAR |  | This item stores whether the current line is a bill or claim entry. A category value of 1 means claim and 2 means bill. |
| 4 | `BC_HX_DATE` | DATETIME |  | The date the statement or claim was processed. This can be NULL when an insurance payment posts and it can’t find a matching claim with that payer in the history. |
| 5 | `BC_HX_COVERAGE_ID` | NUMERIC |  | The unique ID of the coverage that is associated with the bill or claim run |
| 6 | `BC_HX_ASSIGNED_YN` | VARCHAR |  | Indicates whether or not the coverage is assigned to insurance for this transaction. Y indicates the coverage is assigned. |
| 7 | `BC_HX_AMOUNT` | NUMERIC |  | The amount of the transaction on the bill or claim. |
| 8 | `BC_HX_INVOICE_NUM` | VARCHAR |  | The invoice number for the bill or claim. |
| 9 | `BC_HX_PAYMENT_AMT` | NUMERIC |  | Payment amount for payment associated with this invoice. This field applies to claims only. |
| 10 | `BC_HX_PAYMENT_DATE` | DATETIME |  | Payment date for payment associated with this invoice. This field applies to claims only. |
| 11 | `BC_HX_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 12 | `BC_HX_RESUBMIT_DATE` | DATETIME |  | Resubmit date for this claim. This field applies to claims only. |
| 13 | `BC_HX_CLM_DB_ID` | NUMERIC |  | The unique ID of the claim information record for this claim. This field applies to claims only. |
| 14 | `BC_HX_HELD_AMOUNT` | VARCHAR |  | Amount held (not shown) on a bill. This item applies to bills only. |
| 15 | `BC_HX_BO_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 16 | `BC_HX_AUX_PROC` | VARCHAR |  | Claim Auxiliary Procedure. This item is only used by claims. This is populated when claim bundling grouping rules are used and there are procedures that are left over from the claim. This item is a semicolon delimited list of extra procedures. For example, if the bundling rule is set up to bundle and 99212 and a 99213 and there are two 99212s and one 99213, then the 99212 procedure identifier would appear in this column. |
| 17 | `BC_HX_ACCEPT_DATE` | DATETIME |  | Accept date for bill or claim |
| 18 | `BC_HX_FIRST_CLM_FLG` | VARCHAR |  | This item is only populated for claim history lines other than the first. If a previous statement-claim history line is also a claim, it is set to zero. Otherwise, if all previous statement-claim history lines are statements instead, it is set to one. |
| 19 | `BC_HX_AR_CLASS_C_NAME` | VARCHAR |  | AR classification at the time of claim/statement run acceptance. |
| 20 | `BC_HX_ACCEPT_DTTM` | DATETIME (UTC) |  | The UTC date and time the statement or claim was accepted. |
| 21 | `BC_HX_CLM_IS_EXPRESS_YN` | VARCHAR |  | Denotes if the claim is an express claim |
| 22 | `BC_HX_INVOICE_ID` | NUMERIC |  | This stores the Invoice ID of the claim sent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

