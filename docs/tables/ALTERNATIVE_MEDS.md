# ALTERNATIVE_MEDS

> This table contains information about alternative medications selected for patients.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 29  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | ID of the deployment owner for this contact. |
| 6 | `ALT_MED_ORIG_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 7 | `ALT_MED_OPTION_C_NAME` | VARCHAR |  | Alternative medication option taken. |
| 8 | `ALT_MED_USER_ID` | VARCHAR |  | ID of user who ordered the alternative medication. |
| 9 | `ALT_MED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `ALT_MED_TIME` | DATETIME (Attached) |  | Instant the alternative was taken. |
| 11 | `ALT_MED_MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 12 | `ALT_MED_SIG` | VARCHAR |  | Signature field for the alternative medication. |
| 13 | `ALT_MED_QUANTITY` | VARCHAR |  | Quantity for alternative medication. |
| 14 | `ALT_MED_REFILL` | VARCHAR |  | The number of refills for the alternative medication. |
| 15 | `ALT_MED_END_DATE` | VARCHAR |  | End date entered for alternative medication. |
| 16 | `ALT_MED_ORD_CLS_C_NAME` | VARCHAR | org | Order class for alternative medication. |
| 17 | `ALT_MED_REL_COST` | VARCHAR |  | Relative cost of alternative medication. |
| 18 | `ALT_MED_DOSE` | VARCHAR |  | Dose information for alternative medication. |
| 19 | `ALT_MEDS_ROUTE_C_NAME` | VARCHAR | org | Route information for alternative medication. |
| 20 | `ALT_MED_FREQ_ID` | VARCHAR |  | Frequency of alternative medication. |
| 21 | `ALT_MED_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 22 | `ALT_MEDS_DOSE_UNIT` | VARCHAR |  | Dose unit for the alternative medication. |
| 23 | `ALT_MEDS_UNITS_C_NAME` | VARCHAR | org | Unit category for the dose unit of the alternative medication. |
| 24 | `ALT_MED_CONTINUE_C_NAME` | VARCHAR | org | Reason to continue with original order |
| 25 | `ALT_MEDICATIONS_LMA_ID` | NUMERIC |  | Alternative medication (LMA) ID. |
| 26 | `ALT_MEDICATIONS_LMA_ID_ALTERNATIVE_NAME` | VARCHAR |  | This column contains the name of the alternative medication and procedure records. |
| 27 | `ALT_MED_ORIG_SUM_TEXT` | VARCHAR |  | Contains the order summary text of the original order that triggered the LMA. |
| 28 | `ALT_MED_FB_DISC_C_NAME` | VARCHAR |  | Captures the discrete positive/negative medication alternatives feedback value. |
| 29 | `ALT_MED_FB_COMMENT` | VARCHAR |  | Captures freetext feedback comments on the medication alternative. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

