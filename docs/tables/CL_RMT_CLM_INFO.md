# CL_RMT_CLM_INFO

> This table contains the invoice level information to which the payment in the remittance record is posted.

**Primary key:** `IMAGE_ID`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | This is the ID for the remittance image record. |
| 2 | `INV_NO` | VARCHAR |  | The invoice number for the remittance image. |
| 3 | `CLM_STAT_CD_C_NAME` | VARCHAR |  | This is the code identifying the status of an entire claim. |
| 4 | `CLAIM_CHRG_AMT` | NUMERIC |  | This is the amount for submitted charges on this claim. |
| 5 | `CLAIM_PAID_AMT` | NUMERIC |  | This is the amount paid on the claim. |
| 6 | `PAT_RESP_AMT` | NUMERIC |  | This is the patient responsibility amount for the claim. |
| 7 | `CLM_FILING_CODE_C_NAME` | VARCHAR |  | This is a code identifying the type of claim. |
| 8 | `ICN_NO` | VARCHAR |  | This is the payer's internal control number for the claim. |
| 9 | `FAC_CODE_VAL` | VARCHAR |  | This is the facility code used when the submitted code has been modified through adjudication. |
| 10 | `CLAIM_FREQ_C_NAME` | VARCHAR |  | This is the frequency code of the claim. |
| 11 | `DRG_CODE` | VARCHAR |  | This is the Diagnosis Related Group (DRG) code indicating a patient's diagnosis group based on a patient's illnesses, diseases, and medical problems. |
| 12 | `DRG_WGT` | NUMERIC |  | The diagnosis related group weight. |
| 13 | `DISCHRG_FRAC` | NUMERIC |  | The discharge fraction expressed as a decimal. |
| 14 | `FILE_INV_NUM` | VARCHAR |  | Contains the actual invoice number that came in the file. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

