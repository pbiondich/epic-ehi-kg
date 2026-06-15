# AP_CLAIM_PX_SL_LEVELS

> This table contains the allowed amount adjudication levels for AP Claim service lines before stop loss was applied. To link this table’s service line information back to a claim header, join this table to AP_CLAIM_PROC_IDS on the TX_ID column. If you need to report on claim service lines specific to Cost Sharing Reduction (CSR), join this table instead to AP_CLAIM_PROC_IDS_CSR on the TX_ID column.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the AP Claim procedure transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PRE_STOP_LOSS_LEVEL` | VARCHAR |  | The allowed amount adjudication levels the procedure would have had if stop loss was not applied. Information from this caret delimited string is parsed out in subsequent columns. |
| 4 | `PRE_STOP_LOSS_PMT_LV` | VARCHAR |  | The level of payment for the allowed amount of the service line on the AP Claim had stop loss not been applied. |
| 5 | `PRE_STOP_LOSS_CVD` | VARCHAR |  | The covered number of procedures or units of the allowed number of procedures or units for the service line of the AP Claim had stop loss not been applied. |
| 6 | `PRE_STOP_LOSS_LM_TYP` | INTEGER |  | The limit type (such as procedure dollar amount or procedure count) of the allowed amount of the service line on the AP Claim had stop loss not been applied. This column is frequently used to link to the ZC_PROV_CONT_LM_TY table. |
| 7 | `PRE_STOP_LOSS_PMT_MECH` | INTEGER |  | The payment mechanism for the allowed amount of the service line on the AP Claim had stop loss not been applied. This column is frequently used to link to the ZC_SVC_PAY_MECH table. |
| 8 | `PRE_STOP_LOSS_FSC` | VARCHAR |  | The ID of the fee schedule used to determine the allowed amount of the service line on the AP Claim had stop loss not been applied. |
| 9 | `PRE_STOP_LOSS_FSC_FEE_SCHEDULE_NAME` | VARCHAR |  | The name of each fee schedule. |
| 10 | `PRE_STOP_LOSS_PRICE` | VARCHAR |  | The price of the service line allowed amount on the AP Claim had stop loss not been applied. |
| 11 | `PRE_STOP_LOSS_RATE` | VARCHAR |  | The Diagnosis Related Group (DRG) rate used in determining the allowed amount of the service line on the AP Claim had stop loss not been applied. |
| 12 | `PRE_STOP_LOSS_HMU` | VARCHAR |  | The ID of the conversion factor table used to price a service line using Relative Value Unit (RVU) pricing had stop loss not been applied. |
| 13 | `PRE_STOP_LOSS_HMU_TABLE_NAME` | VARCHAR |  | The name for the conversion factor table. |
| 14 | `PRE_STOP_LOSS_TOS` | INTEGER |  | The type of service used to get the conversion factor in Relative Value Unit (RVU) pricing had stop loss not been applied. |
| 15 | `PRE_STOP_LOSS_UNITS` | VARCHAR |  | The total number of time units used to determine the price of an anesthesia procedure on an AP Claim had stop loss not been applied. |
| 16 | `PRE_STOP_LOSS_DSCNT` | VARCHAR |  | Discount percentage used in calculating the allowed amount of the service line on the AP Claim had stop loss not been applied. |
| 17 | `PRE_STOP_LOSS_MULT` | VARCHAR |  | The multiplier or conversion factor value used in calculating the allowed amount of the service line on the AP Claim had stop loss not been applied. |
| 18 | `PRE_STOP_LOSS_RVU_VALUE` | VARCHAR |  | The Relative Value Unit (RVU) value of the procedure on the service line of the AP Claim had stop loss not been applied. |
| 19 | `PRE_STOP_LOSS_LPP_CMMT` | VARCHAR |  | The comment added by the pricing extension, which was used to determine the allowed amount of the service line on the AP Claim had stop loss not been applied. |
| 20 | `PRE_STOP_LOSS_FSM` | NUMERIC |  | The ID of the fee schedule map used to determine the allowed amount of the service line on the AP Claim had stop loss not been applied. |
| 21 | `PRE_STOP_LOSS_FSM_FEE_SCHEDULE_MAP_NAME` | VARCHAR |  | The name for the fee schedule map record. |
| 22 | `PRE_STOP_LOSS_ZIP` | VARCHAR |  | When a fee schedule map is used to determine the allowed amount of the service line on the AP claim, this column contains the postal code where the service was performed had stop loss not been applied. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

