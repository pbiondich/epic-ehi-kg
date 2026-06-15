# CLM_EDIT_WQ_CLM

> This table contains the basic information pertaining to a claim in a claim edit workqueue. Rows for claims still in the error pool will be updated. Note that there are two date fields: EXTRACT_DATE indicates the most recent update where a claim was in the error pool. CLM_PROCESS_DATE indicates when the claim was originally processed and entered the error pool.

**Primary key:** `CLP_ID`  
**Columns:** 22  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLP_ID` | NUMERIC | PK | The ID of the claim record that entered the claim edit workqueue. |
| 2 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 3 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 4 | `PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 5 | `BENEFIT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 6 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 7 | `COVERAGE_ID` | NUMERIC | FK→ | The coverage ID that appears on the claim. |
| 8 | `ACCOUNT_ID` | NUMERIC | FK→ | The account ID that appears on the claim. |
| 9 | `TOTAL_CHARGES` | NUMERIC |  | The dollar amount of charges on the claim. |
| 10 | `TOTAL_PAYMENTS` | NUMERIC |  | The dollar amount in payments that appear on the claim. This applies to claims that have already had payments made on them. |
| 11 | `INVOICE_ID` | NUMERIC | FK→ | The ID of the invoice record associated with the claim. |
| 12 | `INVOICE_NUMBER` | VARCHAR |  | The invoice number that appears on the claim. NOTE: This is not the same as the invoice ID. |
| 13 | `POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 14 | `PREDETERMINATION_YN` | VARCHAR |  | Stores a Yes/No indicator that the associated record represents a request for a predetermination of benefits. |
| 15 | `BILL_AREA_ID` | NUMERIC | FK→ | Stores the Bill Area (BIL .1) associated with the claim. |
| 16 | `BILL_AREA_ID_BILL_AREA_NAME` | VARCHAR |  | The record name of this bill area, financial subdivision, or financial division. |
| 17 | `TOTAL_DUE` | VARCHAR |  | The total amount due on the claim. |
| 18 | `TOTAL_INS_DUE` | NUMERIC |  | Stores the insurance amount due for the charges on the claim. |
| 19 | `TOTAL_PAT_DUE` | NUMERIC |  | Stores the patient amount due for the charges on the claim. |
| 20 | `TOTAL_NONCVD_AMT` | NUMERIC |  | Stores the total non-covered amount associated with the charges on the claim. |
| 21 | `TOTAL_ADJ_AMT` | NUMERIC |  | Stores the total adjustment amount posted to the charges on the claim. |
| 22 | `PAT_ID` | VARCHAR | FK→ | The patient ID associated with this CLP. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `BILL_AREA_ID` | [V_BIL_ALL](V_BIL_ALL.md) | sole_pk | high |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [CLM_EDIT_WQ_DETAIL](CLM_EDIT_WQ_DETAIL.md) | `CLP_ID` | high |
| [CL_REMIT](CL_REMIT.md) | `CLP_ID` | high |

