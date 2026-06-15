# ALT_DRUG_DOSE_RSN

> Stores information as to why a dose alert was triggered.

**Primary key:** `ALT_CSN_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALT_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this contact. This number is unique across all alerts in the system. |
| 2 | `LINE` | INTEGER | PK | The line count. There may be multiple reasons a dose alert was triggered. |
| 3 | `DEVIATION_FRM_DOSE` | NUMERIC |  | Stores the percent for a dose alert. This is rounded to the nearest percent. How this percent is calculated depends upon the dose alert type, as stored in item 2800. For single and daily dose alerts, this value stores the percent that a dose is either above the maximum or below the minimum recommended. For lifetime dose alerts, this value stores the percent of a certain chemical towards the lifetime limit for that chemical. Currently we do not store a percent for frequency or duration dose alerts. |
| 4 | `ALT_ID` | NUMERIC | FK→ | The unique alert ID for each alert. You could link it to ALERT.ALT_ID to get patient and vendor information in table ALERT. |
| 5 | `DOSE_CHEM_C_NAME` | VARCHAR | org | Store the chemical that triggered a dose alert |
| 6 | `ADMIN_AMOUNT_AFTER` | NUMERIC |  | The total amount that the patient will have received after the administration when the alert is fired. For example, if the patient has received 3.5 g of Acetaminophen within the last 24 hours and the nurse tries to give 650 mg of Acetaminophen to the patient, the alert is fired because we cannot give the patient more than 4 g of Acetaminophen within 24 hours. 3.5 g plus 650 mg will be 4.15 g and 4.15 will be saved in this column and g will be saved in column DOSE_UNIT_C. |
| 7 | `CONTACT_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 8 | `DOSE_THRESHOLD_USED` | INTEGER |  | The percent threshold that triggered a critical or threshold-based hard stop dose warning. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ALT_CSN_ID` | [ALT_HISTORY](ALT_HISTORY.md) | sole_pk | high |
| `ALT_ID` | [ALERT](ALERT.md) | sole_pk | high |

