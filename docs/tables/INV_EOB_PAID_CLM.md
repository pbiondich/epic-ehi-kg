# INV_EOB_PAID_CLM

> This table holds the claim level secondary information for a non-primary claim. It contains the paid amount and other secondary amounts other than claim adjustments (CAS).

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 47

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The invoice record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EOB_CLM_CVG_ID` | NUMERIC |  | This item holds the coverage ID associated with American National Standards Institute secondary information that has been edited. |
| 4 | `EOB_CLM_PAID` | NUMERIC |  | The paid amount. |
| 5 | `EOB_CLM_CONTRACT` | NUMERIC |  | The contract amount. |
| 6 | `EOB_CLM_PAT_REMAIN` | NUMERIC |  | The remaining patient liability amount. |
| 7 | `EOB_CLM_NONCOVERED` | NUMERIC |  | The non-covered amount. |
| 8 | `EOB_CLM_MIA_01` | INTEGER |  | This item holds the value for the covered days. |
| 9 | `EOB_CLM_MIA_02` | NUMERIC |  | The Monetary amount from the adjudication of the claim. |
| 10 | `EOB_CLM_MIA_03` | INTEGER |  | This item holds the value for the lifetime reserve days. |
| 11 | `EOB_CLM_MIA_04` | NUMERIC |  | This is the diagnosis related group adjudication amount for the claim. |
| 12 | `EOB_CLM_MIA_05` | VARCHAR |  | This is the claim payment remark code. |
| 13 | `EOB_CLM_MIA_06` | NUMERIC |  | This is the disproportionate share amount. |
| 14 | `EOB_CLM_MIA_07` | NUMERIC |  | This is the Medicare Secondary Payer pass-through amount. |
| 15 | `EOB_CLM_MIA_08` | NUMERIC |  | This is the Prospective Payment System capital amount. |
| 16 | `EOB_CLM_MIA_09` | NUMERIC |  | This is the Prospective Payment System capital, federal specific portion, Diagnosis Related Group amount. |
| 17 | `EOB_CLM_MIA_10` | NUMERIC |  | This is the Prospective Payment System capital, hospital specific portion, Diagnosis Related Group amount. |
| 18 | `EOB_CLM_MIA_11` | NUMERIC |  | This is the Prospective Payment System capital, disproportionate share, hospital Diagnosis Related Group amount. |
| 19 | `EOB_CLM_MIA_12` | NUMERIC |  | This is the old capital amount |
| 20 | `EOB_CLM_MIA_13` | NUMERIC |  | This is the Prospective Payment System capital indirect medical education claim amount. |
| 21 | `EOB_CLM_MIA_14` | NUMERIC |  | This is the hospital specific Diagnosis Related Group amount. |
| 22 | `EOB_CLM_MIA_15` | INTEGER |  | This is the cost report days for the claim. |
| 23 | `EOB_CLM_MIA_16` | NUMERIC |  | This is the federal specific Diagnosis Related Group amount. |
| 24 | `EOB_CLM_MIA_17` | NUMERIC |  | This is the Prospective Payment System Capital Outlier amount. |
| 25 | `EOB_CLM_MIA_18` | NUMERIC |  | This is the indirect teaching amount. |
| 26 | `EOB_CLM_MIA_19` | NUMERIC |  | This is the professional component amount billed but not payable. |
| 27 | `EOB_CLM_MIA_20` | VARCHAR |  | This is the Claim Payment Remark Code. |
| 28 | `EOB_CLM_MIA_21` | VARCHAR |  | This is the Claim Payment Remark Code. |
| 29 | `EOB_CLM_MIA_22` | VARCHAR |  | This is the Claim Payment Remark Code. |
| 30 | `EOB_CLM_MIA_23` | VARCHAR |  | This is the Claim Payment Remark Code. |
| 31 | `EOB_CLM_MIA_24` | NUMERIC |  | This is the capital exception amount. |
| 32 | `EOB_CLM_MOA_01` | NUMERIC |  | This is the reimbursement rate. |
| 33 | `EOB_CLM_MOA_02` | NUMERIC |  | This is the claim Health Care Financing Common Procedural Coding System payable amount. |
| 34 | `EOB_CLM_MOA_03` | VARCHAR |  | This is the Claim Payment Remark Code. |
| 35 | `EOB_CLM_MOA_04` | VARCHAR |  | This is the Claim Payment Remark Code. |
| 36 | `EOB_CLM_MOA_05` | VARCHAR |  | This is the Claim Payment Remark Code. |
| 37 | `EOB_CLM_MOA_06` | VARCHAR |  | This is the Claim Payment Remark Code. |
| 38 | `EOB_CLM_MOA_07` | VARCHAR |  | This is the Claim Payment Remark Code. |
| 39 | `EOB_CLM_MOA_08` | NUMERIC |  | This is the End Stage Renal Disease payment amount. |
| 40 | `EOB_CLM_MOA_09` | NUMERIC |  | This is the professional component amount billed but not payable. |
| 41 | `EOB_CLM_DATE` | DATETIME |  | The adjudication date. |
| 42 | `EOB_CLM_AMT_D8` | NUMERIC |  | The discount amount. |
| 43 | `EOB_CLM_AMT_DY` | NUMERIC |  | The per day limit. |
| 44 | `EOB_CLM_AMT_F5` | NUMERIC |  | The patient paid amount. |
| 45 | `CLM_EOB_AMT_T` | NUMERIC |  | The sales tax amount. |
| 46 | `EOB_CLM_AMT_T2` | NUMERIC |  | The total amount before taxes. |
| 47 | `EOB_COINS_DAYS` | INTEGER |  | The coinsurance days. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

