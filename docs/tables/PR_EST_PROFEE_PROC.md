# PR_EST_PROFEE_PROC

> Procedure information for the professional fees in the price estimate. Professional fees are generated in Resolute Professional Billing.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 66  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the price estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONTEXT_LINE` | INTEGER |  | References the context information from the table PR_EST_PROFEE_CXT. This information is used to provide more accurate pricing information. |
| 4 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 5 | `MODIFIERS` | VARCHAR |  | The procedure modifiers associated with the service specified in the price estimate. |
| 6 | `QUANTITY` | INTEGER |  | The expected quantity of this procedure. |
| 7 | `CHARGE_AMOUNT` | NUMERIC |  | The expected charge amount for this procedure. This may also be referred to as the billed amount. |
| 8 | `ALLOWED_AMT` | NUMERIC |  | The expected allowed amount specified for this procedure. |
| 9 | `SELF_PAY_AMT` | NUMERIC |  | The expected self-pay amount specified for this procedure. |
| 10 | `TTL_CASE` | INTEGER |  | The total number of cases in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 11 | `TTL_CHRG` | NUMERIC |  | The total charges across all cases in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 12 | `STD_DEV` | NUMERIC |  | The standard deviation for charges between cases in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 13 | `HI_CASE_CHRG` | NUMERIC |  | The highest case charges in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 14 | `LO_CASE_CHRG` | NUMERIC |  | The lowest case charges in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 15 | `TTL_CASE_NO_OUT` | INTEGER |  | After removing outliers, the total number of cases in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 16 | `TTL_CHRG_NO_OUT` | NUMERIC |  | After removing outliers, the total charges across all cases in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 17 | `STD_DEV_NO_OUT` | NUMERIC |  | After removing outliers, the standard deviation for charges between cases in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 18 | `HI_CASE_CHRG_NO_OUT` | NUMERIC |  | After removing outliers, the highest case charges in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 19 | `LO_CASE_CHRG_NO_OUT` | NUMERIC |  | After removing outliers, the lowest case charges in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 20 | `PYR_TTL_CASE` | INTEGER |  | The total number of cases in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 21 | `PYR_TTL_ALLOW_AMT` | NUMERIC |  | The total allowed amounts across all cases in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 22 | `PYR_STD_DEV` | NUMERIC |  | The standard deviation between allowed amounts in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 23 | `PYR_HI_ALLOW_AMT` | NUMERIC |  | The highest allowed amount among all cases in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 24 | `PYR_LO_ALLOW_AMT` | NUMERIC |  | The lowest allowed amount among all cases in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 25 | `PYR_TTL_CASE_NO_OUT` | INTEGER |  | After removing outliers, the total number of cases in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 26 | `PYR_TTL_ALLOW_OUT` | NUMERIC |  | After removing outliers, the total allowed amounts across all cases in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 27 | `PYR_STD_DEV_NO_OUT` | NUMERIC |  | After removing outliers, the standard deviation between allowed amounts in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 28 | `PYR_HI_ALLOW_NO_OUT` | NUMERIC |  | After removing outliers, the highest allowed amount among all cases in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 29 | `PYR_LO_ALLOW_NO_OUT` | NUMERIC |  | After removing outliers, the lowest allowed amount among all cases in the historical summary at the time the estimate was made. For the current summary information, see the PR_HX_... tables. |
| 30 | `SYS_SELF_PAY_AMT` | NUMERIC |  | The system calculated self-pay amount for the professional charge. |
| 31 | `PB_ACTUAL_DISCOUNT_AMT` | NUMERIC |  | Discount amount for estimated service. |
| 32 | `PB_SYSTEM_DISCOUNT_AMT` | NUMERIC |  | System-calculated discount amount for estimated service. |
| 33 | `SYS_CHARGE_AMOUNT` | NUMERIC |  | The system-calculated price for the associated professional charge. |
| 34 | `SYS_ALLOWED_AMT` | NUMERIC |  | The system-calculated allowed amount for the associated professional charge. |
| 35 | `PB_DENTAL_RES_ID` | NUMERIC |  | The dental procedure ID of the associated professional charge for an Estimate that originated from Epic's dental application treatment plan activity. |
| 36 | `PB_HX_CHGOVR_USR_ID` | VARCHAR |  | The user who overrode the price of the associated professional charge on a Dental Estimate. |
| 37 | `PB_HX_CHGOVR_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 38 | `PB_HX_ALLOVR_USR_ID` | VARCHAR |  | The user who overrode the allowed amount of the associated professional charge for a Dental Estimate. |
| 39 | `PB_HX_ALLOVR_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 40 | `PB_HX_SPOVR_USR_ID` | VARCHAR |  | The user who overrode the self-pay amount of the associated professional charge for a Dental Estimate. |
| 41 | `PB_HX_SPOVR_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 42 | `PB_HX_CHGOVR_INST_DTTM` | DATETIME (UTC) |  | The instant when the price of the associated professional charge was overridden for a Dental Estimate. |
| 43 | `PB_HX_ALLOVR_INST_DTTM` | DATETIME (UTC) |  | The instant when the allowed amount of the associated professional charge was overridden for a Dental Estimate. |
| 44 | `PB_HX_SPOVR_INST_DTTM` | DATETIME (UTC) |  | The instant when the self-pay amount of the associated professional charge was overridden for a Dental Estimate. |
| 45 | `PB_HX_CHGADJ_C_NAME` | VARCHAR | org | The reason the price of the associated professional charge was adjusted for a Dental Estimate. |
| 46 | `PB_HX_ALLADJ_C_NAME` | VARCHAR |  | The reason the allowed amount of the associated professional charge was adjusted for a Dental Estimate. |
| 47 | `PB_HX_SPADJ_C_NAME` | VARCHAR |  | The reason the self-pay amount of the associated professional charge was adjusted for a Dental Estimate. |
| 48 | `PB_HX_CHGADJ_CMNT` | VARCHAR |  | The free text comment associated with the price adjustment reason of the associated professional charge for a Dental Estimate. |
| 49 | `PB_HX_ALLADJ_CMNT` | VARCHAR |  | The free text comment associated with the allowed amount adjustment reason of the associated professional charge for a Dental Estimate. |
| 50 | `PB_HX_SPADJ_CMNT` | VARCHAR |  | The free text comment associated with the self-pay amount adjustment reason of the associated professional charge for a Dental Estimate. |
| 51 | `PROC_SVC_TYPE_ID` | VARCHAR |  | Service type of the professional charge used to determine benefits |
| 52 | `PROC_SVC_TYPE_ID_SERVICE_TYPE_NAME` | VARCHAR |  | The name of this benefit service type. |
| 53 | `PB_ADDL_LINE` | INTEGER |  | This item holds a line number of related group 1000, which stores additional information about the charge line. |
| 54 | `PB_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 55 | `PB_MEDICATION_QTY` | NUMERIC |  | The medication quantity used to price a Professional Billing (PB) procedure line. |
| 56 | `PB_MED_UNIT_C_NAME` | VARCHAR | org | The medication unit used to price a Professional Billing (PB) procedure line. |
| 57 | `PB_PROC_TYPE_C_NAME` | VARCHAR |  | The type of charge this procedure line represents. |
| 58 | `PB_PROC_GROUPER` | INTEGER |  | A number that groups different procedure lines together for display and pricing purposes. |
| 59 | `PB_FEE_SCHEDULE_ID` | NUMERIC |  | Holds the fee schedule record that was used for calculating the charge amount for a Professional Billing (PB) procedure line. |
| 60 | `PB_FEE_SCHEDULE_ID_FEE_SCHEDULE_NAME` | VARCHAR |  | The name of each fee schedule. |
| 61 | `DENTAL_UPGRADE_OFFSET_AMT` | NUMERIC |  | The upgrade charge adjustment amount. |
| 62 | `DENTAL_DOWNGRADE_OFFSET_AMT` | NUMERIC |  | The additional self-pay due to downgrade for a given procedure line. |
| 63 | `DENTAL_HMO_COPAY_AMT` | NUMERIC |  | The additional self-pay due to HMO copay for a given procedure line. |
| 64 | `PB_OVERRIDE_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 65 | `PB_OVERRIDE_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 66 | `PB_OVERRIDE_FIN_CLASS_C_NAME` | VARCHAR | org | The financial class selected to find historical data in a professional billing context. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

