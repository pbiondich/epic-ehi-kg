# MLSIG_PAT_TEMPLT_LEVEL_2

> This table is for specific sig lines of multiline sigs.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient order template record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MLSIG_LINK_TO_LVL1` | INTEGER |  | For a medication with differing dosage instructions for specified periods of time, this stores which period or group each sig line belongs to. |
| 4 | `MLSIG_FREQ_ID` | VARCHAR |  | The unique identifier for the frequency record used in each period for a medication with differing dosage instructions for specified periods of time. |
| 5 | `MLSIG_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 6 | `MLSIG_DOSE` | VARCHAR |  | For a medication with differing dosage instructions for specified periods of time, the dose (value or range) for each dosage sig line. |
| 7 | `MLSIG_DOSE_UNIT_C_NAME` | VARCHAR | org | For a medication with differing dosage instructions for specified periods of time, this stores the dose unit for each period. |
| 8 | `MLSIG_DOSE_LIMTYP_C_NAME` | VARCHAR |  | Dose limit type for specific lines of a medication with differing dosage instructions for specified periods of time. |
| 9 | `MLSIG_EXACT_TM` | DATETIME (Local) |  | Stores the exact time for the dosage specified in an individual part of a multiline sig. |
| 10 | `MLSIG_PRN_FLAG_YN` | VARCHAR |  | This item stores PRN flag of the multiline sig dosage part. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

