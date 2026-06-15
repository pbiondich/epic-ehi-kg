# AP_CLAIM_TX_HX

> This table contains the history of service line changes for accounts payable claim records.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 75  
**Org-specific columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TX_HX_TIME_SAVE_TM` | DATETIME (Local) |  | The time the record was saved. |
| 4 | `TX_HX_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 5 | `TX_HX_SVC_FROM_DT` | DATETIME |  | Transaction history service from date. |
| 6 | `TX_HX_SVC_TO_DT` | DATETIME |  | Transaction history service to date. |
| 7 | `TX_HX_PROC_HX` | NUMERIC |  | The history of the procedure on previous versions of the service line. |
| 8 | `TX_HX_DX_CODES` | VARCHAR |  | The history of diagnosis codes on previous versions of the service line. |
| 9 | `TX_HX_AMT_BILLED` | NUMERIC |  | The history of the amount billed on previous versions of the service line. |
| 10 | `TX_HX_ALLOWED_AMT` | NUMERIC |  | The history of the allowed amount on previous versions of the service line. |
| 11 | `TX_HX_PAT_AMT` | NUMERIC |  | Patient portion of the bill. |
| 12 | `TX_HX_WITHHOLDINGS` | NUMERIC |  | The history of the withheld amount on previous versions of the service line. |
| 13 | `TX_HX_DISCOUNTS` | NUMERIC |  | The history of the discount amount on previous versions of the service line. |
| 14 | `TX_HX_NET_PAYABLE` | NUMERIC |  | The history of the net payable amount on previous versions of the service line. |
| 15 | `TX_HX_NUM_ID` | NUMERIC |  | Transaction history number in the claim procedure history. |
| 16 | `TX_HX_TX_TYPE_C_NAME` | VARCHAR |  | AP claims transaction type (for procedure history). |
| 17 | `TX_HX_MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 18 | `TX_HX_REV_CODE_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 19 | `TX_HX_SVC_START_TM` | DATETIME (Local) |  | Transaction history service start time. |
| 20 | `TX_HX_SVC_END_TIME` | DATETIME (Local) |  | Transaction history service end time. |
| 21 | `TX_HX_SVC_ELPSD_TM` | INTEGER |  | Transaction history service elapsed time. |
| 22 | `TX_HX_DRG_CODE_ID` | VARCHAR |  | Diagnosis Related Group (DRG) code history item. |
| 23 | `TX_HX_DRG_CODE_ID_DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |
| 24 | `PX_HX_EOB_COMMENT` | VARCHAR |  | Claim procedure history Explanation of Benefits (EOB) comments. |
| 25 | `TX_HX_POS_TYPES_C_NAME` | VARCHAR | org | Claim procedure history place of service types. |
| 26 | `TX_HX_TOS_C_NAME` | VARCHAR | org | Claim procedure history type of service. |
| 27 | `TX_HX_PRIM_INS_AMT` | NUMERIC |  | Insurance amount from primary for history. |
| 28 | `TX_HX_PRIM_PAT_PRT` | NUMERIC |  | Patient portion from primary for history. |
| 29 | `PX_HX_OVRID_AMT_C` | NUMERIC |  | Procedure history for override allowed amounts. |
| 30 | `PX_HX_OVRID_RSN_C_NAME` | VARCHAR | org | Reason the allowed amount was overridden. |
| 31 | `TX_HX_ALLW_CODES_C_NAME` | VARCHAR |  | Procedure history allowed codes. |
| 32 | `PROC_HX_PAT_CODE_C_NAME` | VARCHAR |  | Procedure history patient portion codes. |
| 33 | `TX_HX_CMPTD_WTHLD` | NUMERIC |  | Computed withholding history. |
| 34 | `TX_HX_WTHLD_MTHD_C_NAME` | VARCHAR |  | Withhold method history. |
| 35 | `TX_HX_WTHLD_RATE` | VARCHAR |  | Withhold rate history. |
| 36 | `TX_HX_INS_AMT` | NUMERIC |  | Net insurance amount history. |
| 37 | `TX_HX_NET_INS_AMT` | NUMERIC |  | Net Insurance amount history |
| 38 | `TX_HX_COMPUTED_ADJ` | NUMERIC |  | Computed adjustment history. |
| 39 | `TX_HX_ACTUAL_ADJ` | NUMERIC |  | Actual adjustment history. |
| 40 | `TX_HX_ADJ_REASON_C_NAME` | VARCHAR | org | Adjustment reason history. |
| 41 | `TX_HX_CODE_EDT_SAV` | NUMERIC |  | Transaction history code edit savings. |
| 42 | `TX_HX_U_AND_C_AMT` | NUMERIC |  | Usual and customary amount history. |
| 43 | `TX_HX_CONTRACT_AMT` | NUMERIC |  | Contractual amount history. |
| 44 | `TX_HX_DISALOWED_AMT` | NUMERIC |  | Disallowed amount history. |
| 45 | `TX_HX_NOT_COVERED` | NUMERIC |  | Not covered history. |
| 46 | `TX_HX_DEDUCTIBLE` | NUMERIC |  | The history of the deductible amount on previous versions of the service line. |
| 47 | `TX_HX_COPAY` | NUMERIC |  | The history of the copay amount on previous versions of the service line. |
| 48 | `TX_HX_COINS` | NUMERIC |  | Co-insurance history. |
| 49 | `TX_HX_PAT_TOTAL` | NUMERIC |  | Patient total history. |
| 50 | `TX_HX_BFR_BEN_PEN` | NUMERIC |  | History before benefit penalty. |
| 51 | `TX_HX_AFTR_BEN_PEN` | NUMERIC |  | History after benefit penalty. |
| 52 | `TX_HX_EXCD_BEN_AMT` | NUMERIC |  | Exceeded benefit amount history. |
| 53 | `TX_HX_OVRIDE_DIS_C_NAME` | VARCHAR | org | Override disallowed reason history. |
| 54 | `TX_HX_OVRD_DA_AMT` | NUMERIC |  | Override disallowed amount history. |
| 55 | `TX_HX_OVRD_NC_AMT` | NUMERIC |  | Override not covered amount history. |
| 56 | `TX_HX_OVRD_DEDUCT` | NUMERIC |  | Override deductible history. |
| 57 | `TX_HX_OVRIDE_COINS` | NUMERIC |  | Override co-insurance history. |
| 58 | `TX_HX_OVRIDE_COPAY` | NUMERIC |  | Override copay history. |
| 59 | `TX_HX_OVRD_PTAMT_C_NAME` | VARCHAR | org | Override patient amount reason history. |
| 60 | `TX_HX_OVRD_PATPO` | NUMERIC |  | Override patient portion history. |
| 61 | `TX_HX_COB_SAV_AMT` | NUMERIC |  | Coordination of Benefits (COB) Saving amount history. |
| 62 | `TX_HX_OVRD_BEN_AMT` | NUMERIC |  | Override exceeded benefit amount for transaction history. |
| 63 | `TX_HX_PRICE_ATTR_C_NAME` | VARCHAR | org | Pricing attribute for transaction history. |
| 64 | `TX_HX_PAT_OUTOF_PC` | NUMERIC |  | Patient out of pocket history. |
| 65 | `TX_HX_SAVED_DT` | DATETIME |  | The date the transaction history was saved. |
| 66 | `TX_HX_USER_ID` | VARCHAR |  | Specifies the transaction history user. |
| 67 | `TX_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 68 | `TX_HX_UBC_REVCOD_ID` | VARCHAR |  | This column holds the transaction history for revenue codes in UB Claims. It stores the record ID (this is found in the revenue code master file; it is not the actual revenue code) for revenue codes that were previously entered on the claim. |
| 69 | `TX_HX_UBC_REVCOD_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 70 | `TX_HX_REIMB_AMT` | NUMERIC |  | Healthcare reimbursement amount history. |
| 71 | `TX_HX_OVRD_RIMB_AMT` | NUMERIC |  | Override reimbursement amount history. |
| 72 | `TX_HX_SYS_ADJ_RSN_C_NAME` | VARCHAR |  | System adjustment reason history. |
| 73 | `TX_HX_AFT_BEN_PEN_OVRIDE` | NUMERIC |  | Override after benefits penalty history. |
| 74 | `TX_HX_AFT_BEN_PEN_OVRIDE_RSN_C_NAME` | VARCHAR | org | Override after benefits penalty reason history. This should be translated using ZC_PEN_AFT_BEN_OVRIDE_RSN. |
| 75 | `TX_HX_COB_SAVINGS_PAYOUT` | NUMERIC |  | COB savings payout history |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

