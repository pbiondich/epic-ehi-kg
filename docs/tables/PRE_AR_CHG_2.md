# PRE_AR_CHG_2

> This table is a continuation of the PRE_AR_CHG table. This table contains one row for each line of each temporary accounts receivable (TAR) record (think of a TAR record as one charge entry screen and each line as an individual procedure). Deleting charge lines will delete rows from this table. This table contains additional information about the procedure.

**Overflow of:** [PRE_AR_CHG](PRE_AR_CHG.md)  
**Primary key:** `TAR_ID`, `CHARGE_LINE`  
**Columns:** 65  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `CHARGE_LINE` | INTEGER | PK | The line number for the information associated with this transaction record. This represents a single charge procedure in the transaction. |
| 3 | `PENDING_STATUS_C_NAME` | VARCHAR |  | The pending status of this transaction: 1 means Pending and 2 means Waiting to Pend. If blank, the transaction is not pending. |
| 4 | `TX_TYPE_C_NAME` | VARCHAR |  | What this transaction record is used for (e.g. charge, payment, adjustment, etc...). |
| 5 | `PENDING_REASON_C_NAME` | VARCHAR | org | The pending reason category ID for the temporary transaction. |
| 6 | `PENDING_COMMENT` | VARCHAR |  | A free-text comment to further explain why this transaction is pending. |
| 7 | `LAST_EDITED_DATE` | VARCHAR |  | The last date the check payment was edited. |
| 8 | `HOSP_ACCOUNT_ID` | VARCHAR |  | This item stores the hospital account record ID for the transaction. |
| 9 | `EXT_BILLING_NUM` | VARCHAR |  | A billing number from an external billing system. |
| 10 | `EXT_REFERENCE_NUM` | VARCHAR |  | A reference number from an external billing system. |
| 11 | `ENC_TYPE_C_NAME` | VARCHAR | org | The kind of encounter which is associated with this transaction (e.g. Walk-In, Appointment, Anesthesia, etc...). |
| 12 | `PROV_SPECIALTY_C_NAME` | VARCHAR | org | The provider's area of expert knowledge which applies for this transaction. |
| 13 | `DEFAULT_SVC_DATE` | DATETIME |  | The service date when this transaction took place. |
| 14 | `DO_NOT_BILL_INS_YN` | VARCHAR |  | Do Not Bill Insurance for the charge session (taken from visit if encounter form # is used). Possible values will be "Y" and "N". |
| 15 | `CHARGE_DESC_OVRIDE` | VARCHAR |  | Holds the charge description if it has been changed from the default. |
| 16 | `PROC_MED_NEC_YN` | VARCHAR |  | Indicates whether this particular charge line is a medical necessity or not. Possible values will be "Y" and "N". |
| 17 | `COPAY_INDICATOR_C_NAME` | VARCHAR |  | The payment type for this copay. |
| 18 | `TAX` | NUMERIC |  | The tax related to this charge. |
| 19 | `TAX_PROC_YN` | VARCHAR |  | Indicates whether the procedure line is a tax procedure |
| 20 | `DX_ID` | VARCHAR | FK→ | The diagnoses which apply to this charge line. This will be in the form of comma-separated integers, where each integer corresponds with a line in the CHG_REVIEW_DX table for this transaction. |
| 21 | `MANUAL_PRICE_OVRIDE` | INTEGER |  | Indicates if this price override is a manual override or was due to a pricing contract. |
| 22 | `ADJ_AMT` | NUMERIC |  | Adjustment amount for one charge line. |
| 23 | `PRICE_OVRIDE_FLAG` | NUMERIC |  | Holds the price override for this line, if one has been set. |
| 24 | `PANEL_PROC_ID` | VARCHAR |  | The procedure number for this charge line. Corresponds to the Procedure Master # (EAP-100). |
| 25 | `HEMATOCRIT_READING` | NUMERIC |  | The hematocrit reading for this procedure, if one has been taken. |
| 26 | `HEMOGLOBIN_READING` | NUMERIC |  | The hemoglobin reading for this procedure, if one has been taken. |
| 27 | `CHG_NOT_BILL_INS_YN` | VARCHAR |  | Do Not Bill Insurance for charge line. Possible values will be "Y" and "N". |
| 28 | `CHARGE_LENGTH` | INTEGER |  | The length of time in minutes that this procedure took. |
| 29 | `START_TIME` | DATETIME (Local) |  | The time when this procedure was started. |
| 30 | `STOP_TIME` | DATETIME |  | The time when this procedure was finished. |
| 31 | `START_DATE` | DATETIME |  | The date when this procedure was started. |
| 32 | `STOP_DATE` | DATETIME |  | The date when this procedure was finished. |
| 33 | `SERVICE_TIME` | DATETIME (Local) |  | The time of service for a charge line. |
| 34 | `SELF_PAY_AMOUNT` | NUMERIC |  | The self-pay amount associated with this charge line as determined by the Benefits Engine. |
| 35 | `CLAIM_ID` | NUMERIC | FK→ | The unique ID of the claim information record associated with this charge line. |
| 36 | `CHG_CVG_STAT_C_NAME` | VARCHAR |  | The coverage status category ID for the temporary transaction. This is determined by the Benefits Engine. |
| 37 | `OLD_ETR_ID` | VARCHAR |  | The unique Accounts Receivable (AR) transaction ID which is associated with this charge record. This column is frequently used to link to the ARPB_TRANSACTIONS table. |
| 38 | `ANESTHESIA_TYPE_C_NAME` | VARCHAR | org | Anesthesia procedure type. |
| 39 | `EMERG_STATUS_YN` | VARCHAR |  | Indicates where this charge is associated with an admitted patient with an emergency status. |
| 40 | `PHYSICAL_STATUS_C_NAME` | VARCHAR | org | Physical status of the patient who had the anesthesia procedure. |
| 41 | `ANES_BASE_UNITS` | NUMERIC |  | Anesthesia base units for the charge procedure. |
| 42 | `EMERG_UNITS` | NUMERIC |  | Emergency units for the charge procedure. |
| 43 | `PHYSICAL_STAT_UNITS` | NUMERIC |  | Physical status units for the charge procedure. |
| 44 | `AGE_UNITS` | NUMERIC |  | Age units for the anesthesia procedure. |
| 45 | `ANES_AGE_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 46 | `ANES_EMERG_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 47 | `CHARGE_BILL_STS_C_NAME` | VARCHAR |  | The anesthesia billing status category ID for the temporary transaction. |
| 48 | `ANES_SUPP_UNITS` | VARCHAR |  | Anesthesia supplemental units. |
| 49 | `ANES_AGE_PROC_UNIT` | NUMERIC |  | Anesthesia age unit procedure unit. |
| 50 | `ANES_EMERG_PROC_UNT` | NUMERIC |  | Anesthesia emergency unit procedure unit. |
| 51 | `ORIG_ANES_TX_SS` | VARCHAR |  | Original anesthesia transaction for special supplemental. |
| 52 | `RAD_THER_END` | INTEGER |  | Indicates end of radiation treatment. |
| 53 | `RAD_THER_LINK` | VARCHAR |  | Radiation therapy link for transfer/retro. |
| 54 | `CHANGED_DX_PX_YN` | VARCHAR |  | Indicates if charge review changed the diagnosis or procedure. |
| 55 | `ORIG_PAT_AMT` | NUMERIC |  | Original self-pay amount before discount. |
| 56 | `SST_DISCNT_OVRD_YN` | VARCHAR |  | Flag to indicate that the self-pay discount amount was manually overridden by the user. |
| 57 | `SST_SP_AMT_OVRD_YN` | VARCHAR |  | Flag to indicate that the self-pay amount was overridden in the self-pay discount workflow. |
| 58 | `SST_DISCNT_AMT` | NUMERIC |  | The self-pay discount amount. |
| 59 | `POS_TYPE_OVRRID_C_NAME` | VARCHAR | org | Place of service type override for a single charge line |
| 60 | `BFD_COVERAGE_ID` | NUMERIC |  | This item stores the coverage used to compute reimbursement and pricing contract for charge lines that qualify for bill for denial workflows. |
| 61 | `MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 62 | `WRITE_OFF_EXCEPTION_C_NAME` | VARCHAR |  | The write-off exception for this charge. |
| 63 | `INSURANCE_ONLY_FLAG_C_NAME` | VARCHAR |  | A flag to indicate if insurance only billing applies to this charge. |
| 64 | `AUTO_PAT_WRITEOFF_C_NAME` | VARCHAR |  | This item is set when the user flags the charge line for an automatic patient writeoff, and it is unset if the user unflags the charge line. This allows the system to distinguish when the user was the source of the insurance only flag value, rather than the system having set it automatically. |
| 65 | `DENTAL_PREAUTH_AMT` | NUMERIC |  | Stores the amount that will be sent to insurance for preauthorization for the associated charge line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |
| `DX_ID` | [CLARITY_EDG](CLARITY_EDG.md) | sole_pk | high |

