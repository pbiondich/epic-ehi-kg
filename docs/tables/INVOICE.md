# INVOICE

> This table includes the basic data for the invoice (INV) record. It contains one row for each used INV record (excluding unused pre-allocated invoices). Note that a row in this table can correspond to multiple claims sent.

**Primary key:** `INVOICE_ID`  
**Columns:** 27  
**Joined by:** 54 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK | The Invoice ID. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The patient ID associated with this invoice. |
| 3 | `ACCOUNT_ID` | NUMERIC | FK→ | The account ID that is associated with this invoice. |
| 4 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 5 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 6 | `POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 7 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 8 | `UB_COVERED_DAYS` | INTEGER |  | The number of covered days for a uniform billing claim. |
| 9 | `UB_NON_COVERED_DAYS` | INTEGER |  | The number of non-covered days for a uniform billing claim. |
| 10 | `UB_COINSURANCE_DAYS` | INTEGER |  | The number of coinsurance days for the uniform billing claim. |
| 11 | `UB_PRINCIPA_DIAG_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 12 | `UB_TYPE_OF_BILL_STR` | VARCHAR |  | Stores the type of bill that was sent out on the claim. |
| 13 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 14 | `ACCT_SERIAL_NUM` | INTEGER |  | Stores the account serial number associated with the invoice. |
| 15 | `PAT_SERIAL_NUM` | INTEGER |  | Stores the patient serial number associated with the invoice. |
| 16 | `RQG_ID` | NUMERIC |  | Stores the requisition grouper ID associated with the invoice when there is no patient record. |
| 17 | `TAX_ID` | VARCHAR | FK→ | Stores the tax ID associated with the invoice. |
| 18 | `TAX_ID_TYPE` | VARCHAR |  | Stores the type of tax ID associated with the invoice. |
| 19 | `TREATMENT_PLAN_ID` | VARCHAR | shared | Stores the treatment plan ID associated with the invoice. |
| 20 | `INSURANCE_AMT` | NUMERIC |  | Stores the insurance amount for the invoice. |
| 21 | `SELF_PAY_AMT` | NUMERIC |  | Stores the initial self-pay amount for the invoice. |
| 22 | `INIT_INSURANCE_BAL` | NUMERIC |  | Stores the initial insurance amount for the invoice. |
| 23 | `INIT_SELF_PAY_BAL` | NUMERIC |  | Stores the initial self-pay amount for the invoice. |
| 24 | `BILL_AREA_ID` | NUMERIC | FK→ | Stores the bill area associated with the invoice. |
| 25 | `BILL_AREA_ID_BILL_AREA_NAME` | VARCHAR |  | The record name of this bill area, financial subdivision, or financial division. |
| 26 | `PB_HOSP_ACT_ID` | NUMERIC |  | The Professional Billing Hospital Account ID. |
| 27 | `RECORD_STATUS_C_NAME` | VARCHAR |  | This column shows the status of the invoice record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `BILL_AREA_ID` | [V_BIL_ALL](V_BIL_ALL.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `TAX_ID` | [TAX_INFO](TAX_INFO.md) | sole_pk | high |

## Joined in — referenced by (54)

| From | Column | Confidence |
|------|--------|------------|
| [AUTHORIZATION_TYPE](AUTHORIZATION_TYPE.md) | `INVOICE_ID` | high |
| [AUTH_AUTH_FULL_REFERRAL](AUTH_AUTH_FULL_REFERRAL.md) | `INVOICE_ID` | high |
| [AUTH_NUM_SOURCE](AUTH_NUM_SOURCE.md) | `INVOICE_ID` | high |
| [AUTH_REF_FULL_REFERRAL](AUTH_REF_FULL_REFERRAL.md) | `INVOICE_ID` | high |
| [AUTH_RFL_RECORD_SOURCE](AUTH_RFL_RECORD_SOURCE.md) | `INVOICE_ID` | high |
| [AUTH_SOURCE_AUTH](AUTH_SOURCE_AUTH.md) | `INVOICE_ID` | high |
| [AUTH_SOURCE_CLAIM_INFO](AUTH_SOURCE_CLAIM_INFO.md) | `INVOICE_ID` | high |
| [AUTH_SOURCE_HSP_ACCT](AUTH_SOURCE_HSP_ACCT.md) | `INVOICE_ID` | high |
| [AUTH_SOURCE_REFERRAL](AUTH_SOURCE_REFERRAL.md) | `INVOICE_ID` | high |
| [AUTH_SOURCE_TREAT_PLAN](AUTH_SOURCE_TREAT_PLAN.md) | `INVOICE_ID` | high |
| [CLM_EDIT_WQ_CLM](CLM_EDIT_WQ_CLM.md) | `INVOICE_ID` | high |
| [INVOICE_APC](INVOICE_APC.md) | `INVOICE_ID` | high |
| [INVOICE_APC_TX](INVOICE_APC_TX.md) | `INVOICE_ID` | high |
| [INVOICE_CLM_LN](INVOICE_CLM_LN.md) | `INVOICE_ID` | high |
| [INVOICE_FLAGS](INVOICE_FLAGS.md) | `INVOICE_ID` | high |
| [INVOICE_HX](INVOICE_HX.md) | `INVOICE_ID` | high |
| [INVOICE_INFO](INVOICE_INFO.md) | `INVOICE_ID` | high |
| [INV_ATTACHMENTS](INV_ATTACHMENTS.md) | `INVOICE_ID` | high |
| [INV_AUTH_INFO](INV_AUTH_INFO.md) | `INVOICE_ID` | high |
| [INV_CLM_ICN](INV_CLM_ICN.md) | `INVOICE_ID` | high |
| [INV_CLM_ICN_LIST](INV_CLM_ICN_LIST.md) | `INVOICE_ID` | high |
| [INV_CLM_LN_ADDL](INV_CLM_LN_ADDL.md) | `INVOICE_ID` | high |
| [INV_CLM_LN_ETRS](INV_CLM_LN_ETRS.md) | `INVOICE_ID` | high |
| [INV_COND_CODE](INV_COND_CODE.md) | `INVOICE_ID` | high |
| [INV_DX_INFO](INV_DX_INFO.md) | `INVOICE_ID` | high |
| [INV_EOB_CAS_CLM](INV_EOB_CAS_CLM.md) | `INVOICE_ID` | high |
| [INV_EOB_CAS_LINE](INV_EOB_CAS_LINE.md) | `INVOICE_ID` | high |
| [INV_EOB_LN_REMIT_LINES](INV_EOB_LN_REMIT_LINES.md) | `INVOICE_ID` | high |
| [INV_EOB_PAID_CLM](INV_EOB_PAID_CLM.md) | `INVOICE_ID` | high |
| [INV_EOB_PAID_LINE](INV_EOB_PAID_LINE.md) | `INVOICE_ID` | high |
| [INV_MEA_INFO](INV_MEA_INFO.md) | `INVOICE_ID` | high |
| [INV_NDC_INFO](INV_NDC_INFO.md) | `INVOICE_ID` | high |
| [INV_OCCUR_DATA](INV_OCCUR_DATA.md) | `INVOICE_ID` | high |
| [INV_OCCUR_SPAN](INV_OCCUR_SPAN.md) | `INVOICE_ID` | high |
| [INV_OTH_PROV_ID](INV_OTH_PROV_ID.md) | `INVOICE_ID` | high |
| [INV_OTH_PROV_TYPE](INV_OTH_PROV_TYPE.md) | `INVOICE_ID` | high |
| [INV_PMT_RECOUP](INV_PMT_RECOUP.md) | `INVOICE_ID` | high |
| [INV_PROC_LIST](INV_PROC_LIST.md) | `INVOICE_ID` | high |
| [INV_VALUE_CODE](INV_VALUE_CODE.md) | `INVOICE_ID` | high |
| [LN_AUTHORIZATION_TYPE](LN_AUTHORIZATION_TYPE.md) | `INVOICE_ID` | high |
| [LN_AUTH_AUT_FULL_REFERRAL](LN_AUTH_AUT_FULL_REFERRAL.md) | `INVOICE_ID` | high |
| [LN_AUTH_NUM_SOURCE](LN_AUTH_NUM_SOURCE.md) | `INVOICE_ID` | high |
| [LN_AUTH_REF_FULL_REFERRAL](LN_AUTH_REF_FULL_REFERRAL.md) | `INVOICE_ID` | high |
| [LN_AUTH_RFL_RECORD_SOURCE](LN_AUTH_RFL_RECORD_SOURCE.md) | `INVOICE_ID` | high |
| [LN_AUTH_SOURCE_AUTH](LN_AUTH_SOURCE_AUTH.md) | `INVOICE_ID` | high |
| [LN_AUTH_SOURCE_CLAIM_INFO](LN_AUTH_SOURCE_CLAIM_INFO.md) | `INVOICE_ID` | high |
| [LN_AUTH_SOURCE_HSP_ACCT](LN_AUTH_SOURCE_HSP_ACCT.md) | `INVOICE_ID` | high |
| [LN_AUTH_SOURCE_REFERRAL](LN_AUTH_SOURCE_REFERRAL.md) | `INVOICE_ID` | high |
| [LN_AUTH_SOURCE_TREAT_PLAN](LN_AUTH_SOURCE_TREAT_PLAN.md) | `INVOICE_ID` | high |
| [MTP_AUTO_EVAL_DIAGNOSES](MTP_AUTO_EVAL_DIAGNOSES.md) | `INVOICE_ID` | high |
| [PBI_ALL](PBI_ALL.md) | `INVOICE_ID` | high |
| [TX_INVOICES](TX_INVOICES.md) | `INVOICE_ID` | high |
| [V_EHI_PBI_FILTER_STATIC](V_EHI_PBI_FILTER_STATIC.md) | `INVOICE_ID` | high |
| [V_EHI_PBI_PB_INVOICE](V_EHI_PBI_PB_INVOICE.md) | `INVOICE_ID` | high |

