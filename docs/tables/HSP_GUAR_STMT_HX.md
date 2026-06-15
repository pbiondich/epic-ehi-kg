# HSP_GUAR_STMT_HX

> This table contains hospital guarantor statement history information.

**Primary key:** `GUAR_ACCOUNT_ID`, `LINE`  
**Columns:** 39

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GUAR_ACCOUNT_ID` | NUMERIC | PK | This column stores the unique identifier for the guarantor account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STMT_HX_HBP_ID` | NUMERIC |  | This column stores the unique identifier for the statement history print record. |
| 4 | `STMT_FLWUP_LEVEL` | INTEGER |  | This column stores the statement follow-up level. |
| 5 | `STMT_DATE` | DATETIME |  | The date of the statement or detail bill. |
| 6 | `STMT_BATCH_DATE` | DATETIME |  | statement batch date |
| 7 | `STMT_FORM` | VARCHAR |  | The form on which this statement or detail bill was sent. |
| 8 | `STMT_PROR_PART` | NUMERIC |  | This column stores the proration part amount from the statement. |
| 9 | `STMT_PREV_BALANCE` | NUMERIC |  | statement previous balance amt |
| 10 | `STMT_NEW_CHGS` | NUMERIC |  | This column stores the statement new charge amount. |
| 11 | `STMT_NEW_PMTS` | NUMERIC |  | This column stores the statement new payment amount. |
| 12 | `STMT_NEW_ADJS` | NUMERIC |  | This column stores the statement new adjustment amount. |
| 13 | `STMT_AMOUNT_DUE` | NUMERIC |  | statement amount due |
| 14 | `STMT_TOT_CHGS` | NUMERIC |  | statement total charges |
| 15 | `STMT_TOT_PMTS` | NUMERIC |  | statement total payments |
| 16 | `STMT_TOT_ADJS` | NUMERIC |  | statement total adjustments |
| 17 | `STMT_CUR_BALANCE` | NUMERIC |  | statement current balance |
| 18 | `STMT_IS_DEMAND_YN` | VARCHAR |  | This column indicates whether the statement is a demand statement. |
| 19 | `STMT_PREV_DUE` | NUMERIC |  | Previous statement due amt |
| 20 | `STMT_PLAN_TOTAL` | NUMERIC |  | This column stores the statement payment plan total amount. |
| 21 | `STMT_PLAN_BALANCE` | NUMERIC |  | This column stores the statement payment plan balance. |
| 22 | `STMT_PLAN_MONTH` | NUMERIC |  | This column stores the statement payment plan monthly amount. |
| 23 | `STMT_PREV_INS_BAL` | NUMERIC |  | This column stores the previous insurance balance for hospital billing statements. |
| 24 | `STMT_CUR_INS_BAL` | NUMERIC |  | This column stores the hospital billing current insurance balance for hospital billing statements. |
| 25 | `STMT_SP_LEVEL_C_NAME` | VARCHAR |  | The guarantor self-pay follow-up level for the statement. |
| 26 | `STMT_HX_IS_INFO_YN` | VARCHAR |  | Indicates whether the statement was informational for this statement. Y means informational, N means not informational, blank means not informational. |
| 27 | `STMT_EB_PRNT_ID` | NUMERIC |  | Stores the link to the statement print (SBP) record. |
| 28 | `STMT_DVRY_MTD_C_NAME` | VARCHAR |  | Stores how the statement was delivered. |
| 29 | `STMT_FST_VW_DTTM` | DATETIME (UTC) |  | This column stores the date and time when this Hospital Billing statement was first viewed in MyChart by this guarantor. The date and time for this column is stored in Coordinated Universal Time (UTC) and can be converted to local time by using the EFN_UTC_TO_LOCAL Clarity database function. |
| 30 | `STMT_LST_VW_DTTM` | DATETIME (UTC) |  | This column stores the date and time when this Hospital Billing statement was last viewed in MyChart by this guarantor. The date and time for this column is stored in Coordinated Universal Time (UTC) and can be converted to local time by using the EFN_UTC_TO_LOCAL Clarity database function. |
| 31 | `STMT_PAPER_RSN_C_NAME` | VARCHAR |  | Stores the reason why the statement was sent via paper. |
| 32 | `STMT_PRNT_INV_NUM` | VARCHAR |  | This is the invoice number for the statement. |
| 33 | `INV_NUM_BASE` | VARCHAR |  | This is the base for the invoice number. |
| 34 | `INV_NUM_SEQ` | INTEGER |  | This is the sequence for the invoice number. |
| 35 | `INV_NUM_ASGN_DT` | DATETIME |  | This is the date the statement print invoice number was assigned. |
| 36 | `STMT_HX_IS_MYC_NOTIF_YN` | VARCHAR |  | Stores if the statement/detail bill notification was sent via MyChart. |
| 37 | `HB_STMTHX_CNTST_BAL` | NUMERIC |  | Stores the contested balance on the statement. |
| 38 | `HB_STMT_HX_TOT_SCH` | NUMERIC |  | The total amount of all scheduled payments on the statement. |
| 39 | `HB_STMT_HX_PAY_NOW` | NUMERIC |  | The pay now amount on the statement. This is the amount due subtracted by the total scheduled payment amount. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

