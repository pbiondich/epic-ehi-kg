# BPA_FUP_RSH_STUDY

> This table contains the research study used in the advisory follow-up.

**Primary key:** `ALERT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALERT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the med alert record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `BPA_FUP_RSH_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 6 | `BPA_FUP_RSH_STAT_C_NAME` | VARCHAR | org | Stores the research study enrollment status applied from the advisory. |
| 7 | `BPA_FUP_RSH_MYC_YN` | VARCHAR |  | Advisory follow-up action of sending a research MyChart recruitment request |
| 8 | `ALT_CSN_ID` | NUMERIC | FK→ | A unique serial number for this contact. This number is unique across all alerts in the system. |
| 9 | `BPA_FUP_ENROLL_ID` | NUMERIC |  | The unique ID of the research study association that has generated as a follow-up action for this OurPractice advisory. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ALT_CSN_ID` | [ALT_HISTORY](ALT_HISTORY.md) | sole_pk | high |

