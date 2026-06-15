# CLP_EOB_PAID_CLM

> This table holds the claim level secondary information for a non-primary claim. It contains the paid amount and other secondary amounts other than claim adjustments (CAS).

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 47

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the claim print record. |
| 2 | `LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 3 | `EOB_CLM_CVG_ID` | NUMERIC |  | The claim-level explanation of benefits coverage ID. This only populates for secondary claims. |
| 4 | `EOB_CLM_PAID` | NUMERIC |  | This item holds the claim level paid amount. |
| 5 | `EOB_CLM_CONTRACT` | NUMERIC |  | The claim-level contract amount. |
| 6 | `EOB_CLM_PAT_REMAIN` | NUMERIC |  | This item holds the claim level remaining patient reliability amount. |
| 7 | `EOB_CLM_NONCOVERED` | NUMERIC |  | This item holds the claim level non-covered amount. |
| 8 | `EOB_CLM_MIA_01` | INTEGER |  | This is the covered days count. |
| 9 | `EOB_CLM_MIA_02` | NUMERIC |  | This is the other coverage monetary amount. |
| 10 | `EOB_CLM_MIA_03` | INTEGER |  | This is the other coverage lifetime psychiatric days count. |
| 11 | `EOB_CLM_MIA_04` | NUMERIC |  | This is the other coverage Diagnosis Related Group amount. |
| 12 | `EOB_CLM_MIA_05` | VARCHAR |  | This is the other coverage remark code. |
| 13 | `EOB_CLM_MIA_06` | NUMERIC |  | This is the other coverage disproportionate share amount. |
| 14 | `EOB_CLM_MIA_07` | NUMERIC |  | This is the other coverage Medicare Secondary Payer pass-through amount. |
| 15 | `EOB_CLM_MIA_08` | NUMERIC |  | This is the other coverage Prospective Payment System capital amount. |
| 16 | `EOB_CLM_MIA_09` | NUMERIC |  | This is the other coverage Prospective Payment System capital federal specific Diagnosis Related Group amount. |
| 17 | `EOB_CLM_MIA_10` | NUMERIC |  | This is the other coverage Prospective Payment System capital hospital specific Diagnosis Related Group amount. |
| 18 | `EOB_CLM_MIA_11` | NUMERIC |  | This is the other coverage Prospective Payment System capital Disproportionate Share Hospital Diagnosis Related Group amount. |
| 19 | `EOB_CLM_MIA_12` | NUMERIC |  | This is the other coverage old capital amount. |
| 20 | `EOB_CLM_MIA_13` | NUMERIC |  | This is the other coverage Prospective Payment System capital Indirect Medical Education amount. |
| 21 | `EOB_CLM_MIA_14` | NUMERIC |  | This is the other coverage Prospective Payment System operating hospital specific Diagnosis Related Group amount. |
| 22 | `EOB_CLM_MIA_15` | INTEGER |  | This is the other coverage cost report day count. |
| 23 | `EOB_CLM_MIA_16` | NUMERIC |  | This is the other coverage Prospective Payment System federal specific Diagnosis Related Group amount. |
| 24 | `EOB_CLM_MIA_17` | NUMERIC |  | This is the other coverage Prospective Payment System capital outlier amount. |
| 25 | `EOB_CLM_MIA_18` | NUMERIC |  | This is the other coverage claim indirect teaching amount. |
| 26 | `EOB_CLM_MIA_19` | NUMERIC |  | This is the other coverage non-payable professional component billed amount. |
| 27 | `EOB_CLM_MIA_20` | VARCHAR |  | This is the other coverage remark code. |
| 28 | `EOB_CLM_MIA_21` | VARCHAR |  | This is the other coverage remark code. |
| 29 | `EOB_CLM_MIA_22` | VARCHAR |  | This is the other coverage remark code. |
| 30 | `EOB_CLM_MIA_23` | VARCHAR |  | This is the other coverage remark code. |
| 31 | `EOB_CLM_MIA_24` | NUMERIC |  | This is the other coverage Prospective Payment System capital exception amount. |
| 32 | `EOB_CLM_MOA_01` | NUMERIC |  | This is the other coverage Medicare Outpatient Adjudication reimbursement rate. |
| 33 | `EOB_CLM_MOA_02` | NUMERIC |  | This is the other coverage Medicare Outpatient Adjudication Healthcare Common Procedure Coding System payable amount. |
| 34 | `EOB_CLM_MOA_03` | VARCHAR |  | This is the other coverage Medicare Outpatient Adjudication remark code. |
| 35 | `EOB_CLM_MOA_04` | VARCHAR |  | This is the other coverage Medicare Outpatient Adjudication remark code. |
| 36 | `EOB_CLM_MOA_05` | VARCHAR |  | This is the other coverage Medicare Outpatient Adjudication remark code. |
| 37 | `EOB_CLM_MOA_06` | VARCHAR |  | This is the other coverage Medicare Outpatient Adjudication remark code. |
| 38 | `EOB_CLM_MOA_07` | VARCHAR |  | This is the other coverage Medicare Outpatient Adjudication remark code. |
| 39 | `EOB_CLM_MOA_08` | NUMERIC |  | This is the other coverage Medicare Outpatient Adjudication End Stage Renal Disease payment amount. |
| 40 | `EOB_CLM_MOA_09` | NUMERIC |  | This is the other coverage Medicare Outpatient Adjudication non-payable professional component billed amount. |
| 41 | `EOB_CLM_DATE` | DATETIME |  | The claim-level explanation of benefits adjudication date. This only populates for secondary claims. |
| 42 | `EOB_CLM_AMT_D8` | NUMERIC |  | The Coordination of Benefits (COB) discount amount associated with the claim. This only populates for American National Standards Institute (ANSI) 4010 version electronic claims. |
| 43 | `EOB_CLM_AMT_DY` | NUMERIC |  | The Coordination of Benefits (COB) per day amount associated with the claim. This only populates for American National Standards Institute (ANSI) 4010 version electronic claims. |
| 44 | `EOB_CLM_AMT_F5` | NUMERIC |  | The Coordination of Benefits (COB) patient paid amount associated with the claim. This only populates for American National Standards Institute (ANSI) 4010 version electronic claims. |
| 45 | `EOB_CLM_AMT_T` | NUMERIC |  | The Coordination of Benefits (COB) tax amount associated with the claim. This only populates for American National Standards Institute (ANSI) 4010 version electronic claims. |
| 46 | `EOB_CLM_AMT_T2` | NUMERIC |  | The Coordination of Benefits (COB) total before taxes amount associated with the claim. This only populates for American National Standards Institute (ANSI) 4010 version electronic claims. |
| 47 | `EOB_COINS_DAYS` | INTEGER |  | This item holds the coinsurance days pulled forward from a valid payment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

