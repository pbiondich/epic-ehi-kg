# AP_CLAIM_4

> The AP_CLAIM_4 table contains one record for each claim in the managed care system's AP Claims module.

**Overflow of:** [AP_CLAIM](AP_CLAIM.md)  
**Primary key:** `CLAIM_ID`  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim record. |
| 2 | `TOT_ADDL_ADJ` | NUMERIC |  | Stores the total additional adjustments for the claim. |
| 3 | `AP_CLAIM_IMPORT_SOURCE_C_NAME` | VARCHAR |  | Used to define the type of source a claim is imported from to drive reporting on the different use cases a single workflow type may have. |
| 4 | `SOURCE_GROUP_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 5 | `SERVICE_DATE_FROM_LINE_YN` | VARCHAR |  | Indicates whether the service date was received at the header level, or was determined based on service lines. |
| 6 | `NCH_CLAIM_TYPE_C_NAME` | VARCHAR |  | The National Claims History (NCH) code indicating the type of claim submitted. |
| 7 | `PAID_CLM_FILE_INTEREST_AMT` | NUMERIC |  | The total interest amount from the file for an externally paid claim. |
| 8 | `PAID_CLM_FILE_PENALTY_AMT` | NUMERIC |  | The total penalty amount from the file for an externally paid claim. |
| 9 | `BLK_DTA_MESSAGE_ID` | NUMERIC |  | Contains the indexed AMS pointer to the last bulk data message record to impact this CLM. |
| 10 | `REFUND_REASON` | VARCHAR |  | The refund reason for the claim. Will be used on any refund letters generated for the claim. |
| 11 | `PAYER_CLM_IDENT` | VARCHAR |  | Stores the ID assigned to the claim from the payer. Currently in use for claims loaded through DINE. |
| 12 | `AP_CLM_AR_STATUS_C_NAME` | VARCHAR |  | The accounts receivable status of the AP claim. |
| 13 | `CLAIM_CHECK_MAIL_SENT_DATE` | DATETIME |  | The date that the last check was mailed/sent or disbursed. |
| 14 | `CAPITAL_IME_AMOUNT` | NUMERIC |  | The portion of a hospital's Medicare capital payment that is increased to account for indirect medical education costs associated with teaching hospitals. |
| 15 | `OPERATING_IME_AMOUNT` | NUMERIC |  | The portion of a hospital's Medicare operating payment that is increased to account for higher indirect medical education costs associated with teaching hospitals. |
| 16 | `CAPITAL_DSH_AMOUNT` | NUMERIC |  | The portion of a hospital's Medicare capital payment that is increased to compensate teaching hospitals for higher capital costs associated with serving a disproportionate share of low-income patients. |
| 17 | `UNCOMPENSATED_CARE_AMOUNT` | NUMERIC |  | The portion that reimburses a hospital for care provided to uninsured or underinsured patients for which no payment was received. |
| 18 | `OPERATING_DSH_AMOUNT` | NUMERIC |  | The portion of a hospital's Medicare operating payment that is increased to compensate teaching hospitals for higher capital costs associated with serving a disproportionate share of low-income patients. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

