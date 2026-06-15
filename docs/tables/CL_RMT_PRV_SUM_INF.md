# CL_RMT_PRV_SUM_INF

> This table stores the provider summary information for a remittance image record.

**Primary key:** `IMAGE_ID`  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | This is the ID for the remittance image record with related remit claim references. |
| 2 | `PROV_IDENTIFIER` | VARCHAR |  | This is the provider number for the remittance record. |
| 3 | `FACILITY_TYPE` | VARCHAR |  | This is the code identifying the type of facility where services were provided for the claim reimbursed by the remittance record. |
| 4 | `FP_DATE` | DATETIME |  | This is the last day of the provider’s fiscal year. |
| 5 | `TOT_CLAIM_COUNT` | INTEGER |  | This is total number of claims. |
| 6 | `TOT_CLAIM_AMT` | NUMERIC |  | This is the total reported charges for all claims. |
| 7 | `TOT_COV_AMT` | NUMERIC |  | This is the monetary amount for the total covered charges. This is submitted charges less the non-covered charges. |
| 8 | `TOT_NONCOV_AMT` | NUMERIC |  | This is the amount for the total of non-covered charges. |
| 9 | `TOT_DEN_AMT` | NUMERIC |  | This is the monetary amount for the total of denied charges. |
| 10 | `TOT_PROV_AMT` | NUMERIC |  | This is the monetary amount for the total provider payment. The total provider payment amount includes the total of all interest paid. The amount can be less than zero. |
| 11 | `TOT_INT_AMT` | NUMERIC |  | This is the total amount of interest paid. |
| 12 | `TOT_CONT_AMT` | NUMERIC |  | This is the amount for the total contractual adjustment. |
| 13 | `TOT_GRAM_AMT` | NUMERIC |  | This is the amount for the total Gramm-Rudman adjustment. |
| 14 | `TOT_MSP_AMT` | NUMERIC |  | This is the total Medicare Secondary Payer (MSP) primary payor amount. |
| 15 | `TOT_BLOOD_AMT` | NUMERIC |  | This is the total blood deductible amount in dollars. |
| 16 | `TOT_NONLAB_AMT` | NUMERIC |  | This is the summary of non-lab charges. |
| 17 | `TOT_COINS_AMT` | NUMERIC |  | This is the total coinsurance amount. |
| 18 | `HCPCS_AMT` | NUMERIC |  | This is the Health Care Financing Administration Common Procedural Coding System (HCPCS) reported charges. |
| 19 | `HCPCS_PAYABLE` | NUMERIC |  | This is the total Health Care Financing Administration Common Procedural Coding System (HCPCS) payable amount. |
| 20 | `TOTAL_DEDUCT_AMT` | NUMERIC |  | This is the total deductible amount. |
| 21 | `TOT_PROF_AMT` | NUMERIC |  | This is the total professional component amount. |
| 22 | `PAT_MSP_LIABILITY` | NUMERIC |  | This is the total Medicare Secondary Payer (MSP) patient liability met. |
| 23 | `PAT_REIMB_AMT` | NUMERIC |  | This is the total patient reimbursement amount. |
| 24 | `PIP_CLAIM_CNT` | INTEGER |  | This is the total periodic interim payment (PIP) number of claims. |
| 25 | `PIP_ADJ_AMT` | NUMERIC |  | This is the total periodic interim payment (PIP) adjustment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

