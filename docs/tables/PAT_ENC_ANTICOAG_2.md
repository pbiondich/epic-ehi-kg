# PAT_ENC_ANTICOAG_2

> This table contains information related to anticoagulation monitoring encounters. The following columns apply only when using the calendar tracking navigator section (LVN 617) for the anticoagulation encounter: AC_NO_DOSE_GIVEN_YN and AC_NO_INR_YN. There is a related table, EPI_ANTICOAG, for the most recent anticoagulation episode information.

**Overflow of:** [PAT_ENC_ANTICOAG](PAT_ENC_ANTICOAG.md)  
**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 13  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `AC_NO_DOSE_GIVEN_YN` | VARCHAR |  | Tracks if the "Patient was not given dosing instructions" was selected in an anticoagulation encounter. |
| 5 | `AC_NO_INR_YN` | VARCHAR |  | Tracks if "No INR" was selected for dosing in an anticoagulation encounter |
| 6 | `PERCENTAGE_TTR` | NUMERIC |  | The patient's time in therapeutic range (TTR). |
| 7 | `TTR_END_DATE` | NUMERIC |  | The end date used when TTR was calculated. |
| 8 | `TTR_START_DATE` | NUMERIC |  | The start date used for TTR calculation. |
| 9 | `TTR_DAYS_ON_THERAPY` | NUMERIC |  | Number of days of therapy considered for TTR calculation. |
| 10 | `AC_LINKED_ADM_PAT_ENC_CSN_ID` | NUMERIC | FK→ | This items contains the CSN for the linked admission whose discharge instructions we are saving this to encounter |
| 11 | `EPISODE_RETURN_DATE` | DATETIME |  | Tracks the return date set in the episode at the time of linking to the encounter |
| 12 | `AC_SYNCED_ORDER_ID` | NUMERIC |  | Tracks the order ID most recently synced to the anticoagulation tracking calendar |
| 13 | `AC_DOSING_MED_SIMPLE_GENERIC_C_NAME` | VARCHAR | org | Category ID of the simple generic vitamin K antagonist medication being used to dose the patient in an anticoagulation encounter. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AC_LINKED_ADM_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

