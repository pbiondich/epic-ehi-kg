# HSP_ACCT_CLAIM_HAR

> This table contains hospital account claims information extracted from hospital account records.

**Primary key:** `ACCT_ID`  
**Columns:** 13  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital account. |
| 2 | `UB92_COVEREDDAYS` | INTEGER |  | This column stores the UB92 Covered days (inpatient only): the number of days covered by the primary payer, as qualified by the payer organization. |
| 3 | `UB92_NONCOVEREDDAY` | INTEGER |  | This column stores the UB92 Non Covered days (inpatient only): the number of days not covered by the primary payer, as qualified by the payer organization. |
| 4 | `UB92_COINSDAYS` | INTEGER |  | This column stores the UB92 Coinsurance days: Days covered by secondary coverage in addition to primary coverage. |
| 5 | `UB92_RESERVEDAYS` | INTEGER |  | UB92 Lifetime Reserve Days (INPATIENT ONLY): Each beneficiary has a lifetime reserve of 60 additional days after using 90 days of inpatient hospital services during a spell of illness. Lifetime reserve days are not renewable. |
| 6 | `ADMISSION_TYPE_C_NAME` | VARCHAR | org | The admission type category ID for the hospital account. |
| 7 | `ADMISSION_SOURCE_C_NAME` | VARCHAR | org | The admission source (e.g., Physician Referral, Transfer from a Hospital, Information Not Available) for the patient encounter associated with this hospital account. |
| 8 | `UB92_TOB_OVERRIDE` | VARCHAR |  | This column stores the Type of Bill (TOB) override: TOB is a numeric code printed on claims that provide encounter information to a payer. Values entered here will override system settings that normally determine the TOB. |
| 9 | `AUTHORIZATION_NUM` | VARCHAR |  | Authorization Number: Used on claims for identifying patient referrals and affected reimbursements. |
| 10 | `PARTA_EXHAUST_DT` | DATETIME |  | The date on which the patient's Part A benefits are exhausted for this inpatient stay. Part A benefits cover up to 90 inpatient days per stay (plus any lifetime reserve days the patient may opt to use after the 90th day). After these days have been used, Part A claims will be denied. Inpatient Part B claims may be submitted for appropriate services. |
| 11 | `PATIENT_STATUS_C_NAME` | VARCHAR | org | The patient status for the patient associated with this hospital account (e.g., Alive, Dead, Unknown, Discharged to Home or Self Care, Admitted as an Inpatient to this Hospital). |
| 12 | `SHAREABLE_CLAIM_ID` | NUMERIC |  | This column stores the unique identifier for a shareable claim associated with the hospital account. |
| 13 | `NONCVRD_SNF_STAY_YN` | VARCHAR |  | This item indicates whether the Skilled Nursing Facility (SNF) stay billed on this account is non-covered due to not having a prior qualifying inpatient stay. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

