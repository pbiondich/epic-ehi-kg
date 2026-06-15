# BDC_INFO

> This table contains Denial/Remark/Correspondence/Variance/Claim Status Follow-Up information from the Denial/Correspondence (BDC) master file. It includes information about the denial/remark code received or correspondence text as applicable. It also includes some general information about the current state of the record. It does not include the change history information and specific denial information from the explanation of benefits (EOB).

**Primary key:** `BDC_ID`  
**Columns:** 51  
**Org-specific columns:** 4  
**Joined by:** 22 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BDC_ID` | NUMERIC | PK | The unique identifier for the denial/correspondence record. |
| 2 | `BDC_NAME` | VARCHAR |  | BDC Record Name - Denial/Remark/Correspondence Record Name. |
| 3 | `RECORD_TYPE_C_NAME` | VARCHAR |  | The record type category ID for the Denial/Remark/Correspondence. |
| 4 | `BUCKET_ID` | NUMERIC | shared | The Hospital Liability Bucket that the Denial/Remark/Correspondence record is linked to. |
| 5 | `RECORD_STATUS_C_NAME` | VARCHAR | org | The status category ID for the Denial/Remark/Correspondence. |
| 6 | `RECORD_SOURCE_C_NAME` | VARCHAR | org | The source category ID for the Denial/Remark/Correspondence. |
| 7 | `CLAIM_PRINT_ID` | NUMERIC | shared | The ID of the claim print record for the invoice of the denied payment. |
| 8 | `INVOICE_NUMBER` | VARCHAR |  | The invoice number associated with this denial/correspondence. |
| 9 | `GRP_CODE_C_NAME` | VARCHAR | org | This item holds the group code associated with the reason code in a denial correspondence record. |
| 10 | `REMIT_CODE_ID` | VARCHAR | FK→ | The unique ID of the remittance code associated with the record. |
| 11 | `REMIT_CODE_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 12 | `EXTERNAL_CODE` | VARCHAR |  | The external ID of the remittance code associated with this denial/correspondence. |
| 13 | `INV_END_DATE` | DATETIME |  | Ending Date on the invoice linked to the denial/remark. |
| 14 | `SOURCE_PMT_HB_TX_ID` | NUMERIC |  | ID of the Hospital Billing payment transaction that the denial/remark was linked to. |
| 15 | `EXP_ALLOW_AMT` | NUMERIC |  | Expected allowed amount on denial/remark/correspondence record. |
| 16 | `RESOLVE_REASON_C_NAME` | VARCHAR | org | Resolution Category for Denial/Remark/Correspondence if it has been resolved. |
| 17 | `RESOLVE_COMMENTS` | VARCHAR |  | Comments entered with resolution category. |
| 18 | `BDC_RECEIVE_DATE` | DATETIME |  | The date the Denial/Remark/Correspondence was received. |
| 19 | `BDC_COMPLETE_VOID_DATE` | DATETIME |  | The date the Denial/Remark/Correspondence record was completed or voided. |
| 20 | `BDC_REOPEN_DATE` | DATETIME |  | The date the Denial/Remark/Correspondence record was re-opened after being completed. |
| 21 | `PB_INVOICE_ID` | NUMERIC |  | The professional invoice associated with the denial/correspondence record. |
| 22 | `GUARANTOR_ID` | NUMERIC |  | The unique ID of the guarantor associated with the denial/correspondence record. |
| 23 | `DOC_INFO_ID` | VARCHAR | FK→ | The unique ID of the document that is associated with the denial/correspondence record. |
| 24 | `WRITE_OFF_AMT_SYS` | NUMERIC |  | The write off amount calculated by the system. |
| 25 | `WRITE_OFF_AMT_CALC` | NUMERIC |  | The write off amount entered by the user. If that is blank, this is the write off amount calculated by the system. |
| 26 | `DISCREPANCY_AMT_SYS` | NUMERIC |  | The dollar amount that is at risk for a denial or variance. |
| 27 | `CLM_EXT_VAL_ID` | NUMERIC |  | The Claim External Value ID of the Claim Print ID that was denied. |
| 28 | `BILLING_DRG` | VARCHAR |  | This item stores the billing DRG sent on the claim or coded on the account. The billing DRG is looked up first from the claim and then from the account. It can be manually overridden. |
| 29 | `PAYER_RECOMMENDED_DRG` | VARCHAR |  | The user recorded payer recommended DRG from the payment that created the follow-up record. |
| 30 | `FINAL_RESOLUTION_DRG` | VARCHAR |  | The user recorded final resolution DRG. |
| 31 | `EXPECTED_RECOVERY_AMT` | NUMERIC |  | This item contains the amount of the expected payment as a result of resubmitting the claim associated with this denial. |
| 32 | `ACTUAL_RECOVERY_AMT_USER` | NUMERIC |  | This item contains the amount actually paid as a result of resubmitting the claim associated with this denial. This can be overridden. |
| 33 | `WRITE_OFF_AMT_USER` | NUMERIC |  | This item contains the amount of this denial that was written off. |
| 34 | `EXT_PAT_NAME` | VARCHAR |  | This item is used to record the patient name if the record of the patient is in an external system. |
| 35 | `EXT_PAT_MRN` | VARCHAR |  | This item is used to record the patient's medical record number if the record of the patient is in an external system. |
| 36 | `EXT_ADMIT_DATE` | DATETIME |  | This item is used to record the patient admit date if the record of the patient is in an external system. |
| 37 | `EXT_DISCHARGE_DATE` | DATETIME |  | This item is used to record the patient discharge date if the record of the patient is in an external system. |
| 38 | `EXT_CLAIM_NUM` | VARCHAR |  | This item is used to record the claim number if the record of the patient is in an external system. |
| 39 | `EXT_PAT_BIRTH_DATE` | DATETIME |  | This item is used to record the patient's date of birth if the record of the patient is in an external system. |
| 40 | `SOURCE_PMT_PB_TX_ID` | NUMERIC |  | Professional Billing payment transaction which led to denial/correspondence record creation. |
| 41 | `DFLT_CLASS_USES_REMARK_CODE_ID` | VARCHAR |  | Stores the highest priority associated remark code for denials if this remark was used to get default classification items. Default classification items include priority, preventable, owning area, source area, and code category. |
| 42 | `DFLT_CLASS_USES_REMARK_CODE_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 43 | `APPEAL_DEADLINE_DATE` | DATETIME |  | This item stores the initial appeal deadline at the moment the BDC is created. |
| 44 | `PAYER_DOWNGRADE_TYPE_C_NAME` | VARCHAR |  | The type of downgrade requested via this BDC when the primary payer tries to dispute the level of care of the HAR. |
| 45 | `PAYER_DOWNGRADE_OUTCOME_C_NAME` | VARCHAR |  | Whether the primary payer's attempt to lower the level of care of the account via this BDC was appropriate and whether it was overturned or led to a downgrade. This item is null if no such attempt was made by the Primary Payer. |
| 46 | `RECONCILE_CLAIM_STATUS_C_NAME` | VARCHAR |  | The status of a claim when the follow-up was needed. |
| 47 | `INT_CONTROL_NUMBER` | VARCHAR |  | The payer's internal control number (ICN) relevant to a follow-up. The number is provided by the payer in response to a claim, like a claim status message. |
| 48 | `CLAIM_RECON_ID` | VARCHAR |  | The claim reconciliation record ID that was the basis for creating the denial/correspondence record. |
| 49 | `CLAIM_RECON_CSN_ID` | NUMERIC |  | The unique contact serial number of the claim reconciliation contact that was the basis for creating the denial/correspondence record. |
| 50 | `FOLLOW_UP_CONTEXT_C_NAME` | VARCHAR |  | This item documents the context of a follow-up, regardless of the source. The context should indicate why follow-up is needed. |
| 51 | `APPEAL_LLM_TEXT_GENERATED_YN` | VARCHAR |  | Indicates if this denial had a clinical basis for appeal generated by the appeal assistant record or if text generation was attempted but failed. A value of 1 will be assigned if text was generated, 0 if generation failed, and null if generation was not attempted. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DOC_INFO_ID` | [DOC_INFORMATION](DOC_INFORMATION.md) | sole_pk | high |
| `REMIT_CODE_ID` | [CLARITY_RMC](CLARITY_RMC.md) | sole_pk | high |

## Joined in — referenced by (22)

| From | Column | Confidence |
|------|--------|------------|
| [BDC_ADDL_CLAIM_STS_CSN](BDC_ADDL_CLAIM_STS_CSN.md) | `BDC_ID` | high |
| [BDC_ASSOC_REMARK_CODES](BDC_ASSOC_REMARK_CODES.md) | `BDC_ID` | high |
| [BDC_CLAIM_STATUS](BDC_CLAIM_STATUS.md) | `BDC_ID` | high |
| [BDC_LOINC_CODES](BDC_LOINC_CODES.md) | `BDC_ID` | high |
| [BDC_PB_CHGS](BDC_PB_CHGS.md) | `BDC_ID` | high |
| [HSP_BDC_APPEAL_DATES](HSP_BDC_APPEAL_DATES.md) | `BDC_ID` | high |
| [HSP_BDC_CHNG_HX](HSP_BDC_CHNG_HX.md) | `BDC_ID` | high |
| [HSP_BDC_CONTRIB_PMT](HSP_BDC_CONTRIB_PMT.md) | `BDC_ID` | high |
| [HSP_BDC_CPT_CODE](HSP_BDC_CPT_CODE.md) | `BDC_ID` | high |
| [HSP_BDC_CRSPNDNCE](HSP_BDC_CRSPNDNCE.md) | `BDC_ID` | high |
| [HSP_BDC_DENIAL_DATA](HSP_BDC_DENIAL_DATA.md) | `BDC_ID` | high |
| [HSP_BDC_DENIED_DATES](HSP_BDC_DENIED_DATES.md) | `BDC_ID` | high |
| [HSP_BDC_DENIED_DIAGNOSES](HSP_BDC_DENIED_DIAGNOSES.md) | `BDC_ID` | high |
| [HSP_BDC_DSC_RSN_CD](HSP_BDC_DSC_RSN_CD.md) | `BDC_ID` | high |
| [HSP_BDC_IMAGING](HSP_BDC_IMAGING.md) | `BDC_ID` | high |
| [HSP_BDC_LINE_MODIFIERS](HSP_BDC_LINE_MODIFIERS.md) | `BDC_ID` | high |
| [HSP_BDC_PAYOR](HSP_BDC_PAYOR.md) | `BDC_ID` | high |
| [HSP_BDC_PROF_INV](HSP_BDC_PROF_INV.md) | `BDC_ID` | high |
| [HSP_BDC_RECV_TX](HSP_BDC_RECV_TX.md) | `BDC_ID` | high |
| [HSP_BDC_REV_CODE](HSP_BDC_REV_CODE.md) | `BDC_ID` | high |
| [HSP_BDC_WO_ADJ_TX](HSP_BDC_WO_ADJ_TX.md) | `BDC_ID` | high |
| [HSP_BFH_ACTIVITY](HSP_BFH_ACTIVITY.md) | `BDC_ID` | high |

