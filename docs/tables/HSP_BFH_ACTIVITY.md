# HSP_BFH_ACTIVITY

> History of billing activities performed.

**Primary key:** `BFH_ID`  
**Columns:** 31  
**Joined by:** 38 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BFH_ID` | NUMERIC | PK | This column stores the unique identifier for the billing activity history record. |
| 2 | `HB_ACTIVITY_ATM_ID_ATM_NAME` | VARCHAR |  | The name of the billing activity. |
| 3 | `HB_CONTEXT_C_NAME` | VARCHAR |  | Stores the hospital billing context (hospital account, guarantor, and others) category number that the activity was performed from. |
| 4 | `ACTIVITY_DATE` | DATETIME |  | Stores the date an activity was performed. |
| 5 | `ACTIVITY_INST_DTTM` | DATETIME (Local) |  | Stores the instant an activity was performed. |
| 6 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the Hospital Account that this activity was performed on. |
| 7 | `BUCKET_ID` | NUMERIC | shared | This column stores the unique identifier for the liability bucket that this action was performed on. |
| 8 | `ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the guarantor that this activity was performed on. This column is only populated for activities performed in a guarantor context. |
| 9 | `USER_ID` | VARCHAR | FK→ | This column stores the unique identifier for the user who performed this action. |
| 10 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `SYSTEM_YN` | VARCHAR |  | Stores whether this was a system auto action or not. |
| 12 | `BDC_ID` | NUMERIC | FK→ | Stores the follow-up record the activity was performed on. |
| 13 | `HB_MATCHED_SP_AMOUNT` | NUMERIC |  | The total hospital billing matched self-pay amount for the billing activity. |
| 14 | `HB_MATCHED_INS_AMOUNT` | NUMERIC |  | The total hospital billing matched insurance amount for the billing activity. |
| 15 | `PB_MATCHED_SP_AMOUNT` | NUMERIC |  | The total professional billing matched self-pay amount for the billing activity. |
| 16 | `SCHED_PMT_ID` | NUMERIC | FK→ | Stores the scheduled payment record on which a billing activity was performed. |
| 17 | `ACTIVITY_ID_NUMBER` | INTEGER |  | This column stores the unique identifiers for follow-up activities caused by this billing activity. All resultant follow-up activities will have this ID in their System Activity ID (FOL 257) item. |
| 18 | `PB_TOTAL_MATCHED_INS_AMOUNT` | NUMERIC |  | Stores the total Professional Billing matched insurance amount for the billing activity. |
| 19 | `TOTAL_MATCHED_SP_AMOUNT` | NUMERIC |  | Stores the total matched self-pay amount for the billing activity. |
| 20 | `TOTAL_MATCHED_INS_AMOUNT` | NUMERIC |  | Stores the total matched insurance amount for the billing activity. |
| 21 | `MC_PB_ACCT_ID` | VARCHAR |  | This column stores the Premium Billing Account this action was performed on. |
| 22 | `ACTIVITY_COMM_ID` | VARCHAR |  | Contact (CAL) ID to be attached if there is currently a CRM Sidebar open when the Billing Action takes place. |
| 23 | `HB_TX_ID` | NUMERIC |  | Stores the Hospital Transaction that this action was performed on. |
| 24 | `CLAIM_PRINT_ID` | NUMERIC | shared | ID of the claim record the action acted on. |
| 25 | `BILLING_SYSTEM_C_NAME` | VARCHAR |  | The billing system this billing activity was performed for. |
| 26 | `ROI_ID` | VARCHAR |  | ID of the release record the action was performed on. |
| 27 | `INVOICE_NUMBER` | VARCHAR |  | Invoice number of the claim the action was performed on. |
| 28 | `REMIT_ID` | NUMERIC |  | ID of the remittance snapshot (RRT) record the action acted on. |
| 29 | `CLAIM_RUN_CTR_ID` | NUMERIC |  | The ID of the claim run tracking (CTR) record the action acted on. |
| 30 | `RUN_NUMBER` | INTEGER |  | The number of the run the action acted on. |
| 31 | `ACT_SOURCE_C_NAME` | NUMERIC |  | Stores whether this activity was performed by the system, a user, or a patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `BDC_ID` | [BDC_INFO](BDC_INFO.md) | sole_pk | high |
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |
| `SCHED_PMT_ID` | [BILL_SCHED_PMT](BILL_SCHED_PMT.md) | sole_pk | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

## Joined in — referenced by (38)

| From | Column | Confidence |
|------|--------|------------|
| [BFH_XR_AMOUNTS_AFTER](BFH_XR_AMOUNTS_AFTER.md) | `BFH_ID` | high |
| [BFH_XR_AMOUNTS_BEFORE](BFH_XR_AMOUNTS_BEFORE.md) | `BFH_ID` | high |
| [EB_BFH_BDC_RECORDS](EB_BFH_BDC_RECORDS.md) | `BFH_ID` | high |
| [HSP_BDC_CHNG_HX](HSP_BDC_CHNG_HX.md) | `BFH_ID` | high |
| [HSP_BFH_ACT_AFFECT_BKTS](HSP_BFH_ACT_AFFECT_BKTS.md) | `BFH_ID` | high |
| [HSP_BFH_ACT_COD_FLAGS_ADD](HSP_BFH_ACT_COD_FLAGS_ADD.md) | `BFH_ID` | high |
| [HSP_BFH_ACT_COD_FLAGS_RMV](HSP_BFH_ACT_COD_FLAGS_RMV.md) | `BFH_ID` | high |
| [HSP_BFH_ACT_CREATED_BDCS](HSP_BFH_ACT_CREATED_BDCS.md) | `BFH_ID` | high |
| [HSP_BFH_ACT_DATA](HSP_BFH_ACT_DATA.md) | `BFH_ID` | high |
| [HSP_BFH_ACT_DATA_2](HSP_BFH_ACT_DATA_2.md) | `BFH_ID` | high |
| [HSP_BFH_ACT_DATA_BDC](HSP_BFH_ACT_DATA_BDC.md) | `BFH_ID` | high |
| [HSP_BFH_ACT_DATA_BDC_ROI](HSP_BFH_ACT_DATA_BDC_ROI.md) | `BFH_ID` | high |
| [HSP_BFH_ACT_DATA_HLB](HSP_BFH_ACT_DATA_HLB.md) | `BFH_ID` | high |
| [HSP_BFH_ACT_DATA_PBA](HSP_BFH_ACT_DATA_PBA.md) | `BFH_ID` | high |
| [HSP_BFH_ACT_TXS_ADD](HSP_BFH_ACT_TXS_ADD.md) | `BFH_ID` | high |
| [HSP_BFH_ACT_TXS_RMVD](HSP_BFH_ACT_TXS_RMVD.md) | `BFH_ID` | high |
| [HSP_BFH_ACT_UPDATED_BDCS](HSP_BFH_ACT_UPDATED_BDCS.md) | `BFH_ID` | high |
| [HSP_BFH_BILL_RANGE_ALT](HSP_BFH_BILL_RANGE_ALT.md) | `BFH_ID` | high |
| [HSP_BFH_BILL_RANGE_CVG](HSP_BFH_BILL_RANGE_CVG.md) | `BFH_ID` | high |
| [HSP_BFH_BILL_RANGE_END](HSP_BFH_BILL_RANGE_END.md) | `BFH_ID` | high |
| [HSP_BFH_BILL_RANGE_LOC](HSP_BFH_BILL_RANGE_LOC.md) | `BFH_ID` | high |
| [HSP_BFH_BILL_RANGE_START](HSP_BFH_BILL_RANGE_START.md) | `BFH_ID` | high |
| [HSP_BFH_BL_IND_ADD](HSP_BFH_BL_IND_ADD.md) | `BFH_ID` | high |
| [HSP_BFH_BL_IND_RM](HSP_BFH_BL_IND_RM.md) | `BFH_ID` | high |
| [HSP_BFH_DNB_OVERRIDE](HSP_BFH_DNB_OVERRIDE.md) | `BFH_ID` | high |
| [HSP_BFH_EARSTS_ADD](HSP_BFH_EARSTS_ADD.md) | `BFH_ID` | high |
| [HSP_BFH_EARSTS_RM](HSP_BFH_EARSTS_RM.md) | `BFH_ID` | high |
| [HSP_BFH_EPISODE_ADD](HSP_BFH_EPISODE_ADD.md) | `BFH_ID` | high |
| [HSP_BFH_EPISODE_REM](HSP_BFH_EPISODE_REM.md) | `BFH_ID` | high |
| [HSP_BFH_HOSP_TXS](HSP_BFH_HOSP_TXS.md) | `BFH_ID` | high |
| [HSP_BFH_INV_NUM_ADDED](HSP_BFH_INV_NUM_ADDED.md) | `BFH_ID` | high |
| [HSP_BFH_INV_NUM_REMOVED](HSP_BFH_INV_NUM_REMOVED.md) | `BFH_ID` | high |
| [HSP_BFH_PB_REFUND_REASONS](HSP_BFH_PB_REFUND_REASONS.md) | `BFH_ID` | high |
| [HSP_BFH_PROF_TXS](HSP_BFH_PROF_TXS.md) | `BFH_ID` | high |
| [HSP_BFH_SB_ADD](HSP_BFH_SB_ADD.md) | `BFH_ID` | high |
| [HSP_BFH_SB_REMOVE](HSP_BFH_SB_REMOVE.md) | `BFH_ID` | high |
| [HSP_BFH_SELECTED_HAR](HSP_BFH_SELECTED_HAR.md) | `BFH_ID` | high |
| [PB_BFH_FOLLOWUP_RECORDS](PB_BFH_FOLLOWUP_RECORDS.md) | `BFH_ID` | high |

