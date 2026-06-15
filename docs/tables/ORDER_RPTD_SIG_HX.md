# ORDER_RPTD_SIG_HX

> This table contains a history of sig-related data for prescriptions, both what the provider initially prescribed and what the patient later reported taking. Most commonly, the first row for any prescription represents the sig as the prescription was written, and subsequent rows will represent changes in what the patient reports taking.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 24  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 4 | `ENTRY_USER_ID` | VARCHAR |  | The unique identifier of the user who entered the medication instructions. |
| 5 | `ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `ENTRY_DTTM` | DATETIME (Local) |  | The date and time when these medication instructions were entered. |
| 7 | `ACTION_C_NAME` | VARCHAR |  | The action represented by this sig - e.g. the initial prescription; the pharmacist has edited the sig; or the patient reports taking this medication differently from how it was prescribed. |
| 8 | `SOURCE_C_NAME` | VARCHAR |  | The location from which this sig was entered. |
| 9 | `INFORMANT_C_NAME` | VARCHAR | org | The relationship to patient category ID for the person (as related to the patient) who reported the medication instructions for this medication. |
| 10 | `REASON_C_NAME` | VARCHAR | org | The reason given for why the patient is not taking the medication as prescribed. |
| 11 | `REASON_COMMENT` | VARCHAR |  | Additional comments on the reason why the patient is not taking the medication as prescribed. |
| 12 | `DOSE_MIN` | NUMERIC |  | The lower bound of the ranged dose for this medication's instructions. |
| 13 | `DOSE_UNIT_C_NAME` | VARCHAR | org | The med & dose unit category ID for the dose of this medication's instructions. |
| 14 | `FREQUENCY_ID` | VARCHAR |  | The unique identifier of the frequency record used in the medication instructions. |
| 15 | `FREQUENCY_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 16 | `PRN_COMMENT` | VARCHAR |  | The as-needed comment for the medication instructions. |
| 17 | `ROUTE_C_NAME` | VARCHAR | org | The route for this medication instructions. |
| 18 | `INDICATIONS_COMMENT` | VARCHAR |  | Comments about the indications of use for the medication instructions. |
| 19 | `DOSE_MAX` | NUMERIC |  | The upper bound of the ranged dose for this medication's instructions. |
| 20 | `BRUKSOMRADE` | VARCHAR |  | Stores the patient-reported Bruksomåde in Norway |
| 21 | `BRUKSOMRADE_MEDICAL_COND_ID` | NUMERIC |  | Stores the patient-reported Bruksomåde (Discrete) in Norway |
| 22 | `BRUKSOMRADE_MEDICAL_COND_ID_MEDICAL_COND_NAME` | VARCHAR |  | This contains the name of the medical condition. |
| 23 | `RPTSIG_USES_TOD_IN_PAT_SIG_C_NAME` | VARCHAR |  | Whether or not the patient reported frequency included times of day (i.e., the user entering this used time of day checkboxes to document the patient reported frequency). |
| 24 | `PT_TAKING_DIFF_CMTS` | VARCHAR |  | Stores taking differently comments entered by the patient during eCheck-in or Welcome self-arrival. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

