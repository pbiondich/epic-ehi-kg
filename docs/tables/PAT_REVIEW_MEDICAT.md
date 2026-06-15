# PAT_REVIEW_MEDICAT

> Table contains patient entered clinical medication data review from Welcome Kiosk and MyChart.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `PAT_REVIEW_ORD_ID` | NUMERIC |  | Patient medication reviewed by patient. |
| 7 | `PAT_REVIEW_ORD_R_YN` | VARCHAR |  | Patient medication reviewed by patient response. |
| 8 | `PAT_REV_MED_EXTERN` | VARCHAR |  | Patient medications reviewed by the patient, entered in a free text format. |
| 9 | `TAKING_STATUS_C_NAME` | VARCHAR |  | This column stores the taking flag (Taking/Not Taking/Taking Differently) entered by the patient/proxy for a medication during eCheck-in or self-arrival. |
| 10 | `TAKING_DIFF_REASON_C_NAME` | VARCHAR | org | This column stores a reason why the patient reports either not taking a medication or taking it differently than prescribed. |
| 11 | `TAKING_DIFF_COMMENT` | VARCHAR |  | This column stores comments entered by the patient to explain how and why they are taking a med diffferently than prescribed, or not taking it. |
| 12 | `TK_DIFF_SRC_PAT_ENC_CSN_ID` | NUMERIC | FK→ | When a patient selects a previously documented taking differently sig as the way they are currently taking a medication, this column stores the unique contact serial number (CSN) of the patient contact in which that sig was documented. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 13 | `TK_DIFF_SRC_LOCAL_DTTM` | DATETIME (Local) |  | When a patient selects a previously documented taking differently sig as the way they are currently taking a medication, this column stores the timestamp at which that sig was documented. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `TK_DIFF_SRC_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

