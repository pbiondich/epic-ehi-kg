# AP_CLAIM_PX_AMT_LV

> This table contains the allowed amount adjudication levels for AP Claim procedures. To link this table’s service line information back to a claim header, join this table to AP_CLAIM_PROC_IDS on the TX_ID column. If you need to report on claim service lines specific to Cost Sharing Reduction (CSR), join this table instead to AP_CLAIM_PROC_IDS_CSR on the TX_ID column.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the AP Claim procedure transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ALLOW_AMT_ADJ_LVLS` | VARCHAR |  | The allowed amount adjudication levels for the procedure. Information from this caret (^) delimited string is parsed out in subsequent columns. |
| 4 | `ALWD_AMT_LVL_PMT_LV` | VARCHAR |  | The level of payment for the allowed amount of the service line on the AP Claim. |
| 5 | `ALWD_AMT_LVL_CVD` | VARCHAR |  | The covered amount of the allowed amount for the service line of the AP Claim. |
| 6 | `ALWD_AMT_LVL_LM_TYP` | INTEGER |  | The limit type of the allowed amount of the service line on the AP Claim. |
| 7 | `ALWD_AMT_PMT_MECH` | INTEGER |  | The payment mechanism for the allowed amount of the service line on the AP Claim. |
| 8 | `ALWD_AMT_LVL_PRICE` | VARCHAR |  | The price of the service line allowed amount on the AP Claim. |
| 9 | `ALWD_AMT_LVL_RATE` | VARCHAR |  | The rate used in determining the allowed amount of the service line on the AP Claim. |
| 10 | `ALWD_AMT_LVL_HMU` | VARCHAR |  | The conversion factor table used to price a service line using RVU pricing. |
| 11 | `ALWD_AMT_LVL_HMU_TABLE_NAME` | VARCHAR |  | The name for the conversion factor table. |
| 12 | `ALWD_AMT_LVL_TOS` | INTEGER |  | The type of service used to get the conversion factor in Relative Value Unit (RVU) pricing. |
| 13 | `ALWD_AMT_LVL_UNITS` | VARCHAR |  | The total number of time units used to determine the price of an anesthesia procedure on an AP Claim. |
| 14 | `ALWD_AMT_LVL_DSCNT` | VARCHAR |  | Discount percentage used in calculating the allowed amount of the service line on the AP Claim. |
| 15 | `ALWD_AMT_LVL_MULT` | VARCHAR |  | The multiplier or conversion factor value used in calculating the allowed amount of the service line on the AP Claim. |
| 16 | `ALWD_AMT_RVU_VALUE` | VARCHAR |  | The Relative Value Unit (RVU) value of the procedure on the service line of the AP Claim. This is only stored in level 1. |
| 17 | `ALWD_AMT_LPP_CMMT` | VARCHAR |  | The comment added by the pricing programming point, which was used to determine the allowed amount of the service line on the AP Claim. |
| 18 | `ALWD_AMT_LVL_FSM` | NUMERIC |  | The ID of the fee schedule map used to determine the allowed amount of the service line on the AP Claim. |
| 19 | `ALWD_AMT_LVL_FSM_FEE_SCHEDULE_MAP_NAME` | VARCHAR |  | The name for the fee schedule map record. |
| 20 | `ALWD_AMT_LVL_ZIP` | VARCHAR |  | When a fee schedule map is used to determine the allowed amount of the service line on the AP claim, this column contains the ZIP Code where the service was performed. |
| 21 | `ALWD_AMT_LVL_UNSUPP_LPP_YN` | VARCHAR |  | Set to "Y" if the pricing programming point is not supported, resulting in the execution of the pricing programming point being skipped. Set to "N" otherwise. |
| 22 | `ALWD_AMT_LVL_FEE_SCHED1_PRICE` | VARCHAR |  | The rate associated with the first fee schedule used to determine the allowed amount of the service line on the AP Claim. |
| 23 | `ALWD_AMT_LVL_FEE_SCHED2_PRICE` | VARCHAR |  | The rate associated with the second fee schedule used to determine the allowed amount of the service line on the AP Claim. |
| 24 | `ALWD_AMT_SVC_PAYMENT_MECH_C` | INTEGER |  | The payment mechanism used as a result of either minimum of options or maximum of options to determine the allowed amount of the service line on the AP Claim. |
| 25 | `ALWD_AMT_LVL_IS_STOP_LOSS_YN` | VARCHAR |  | Set to "Y" if the level of payment for the allowed amount of the service line on the AP Claim is a stop loss level, "N" otherwise. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

