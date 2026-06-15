# MED_CVG_USERACTION

> This table holds information about user actions taken on Patient Estimates.

**Primary key:** `MED_ESTIMATE_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MED_ESTIMATE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the medication estimate record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `UAC_EMP_ID` | VARCHAR |  | This item stores the user (EMP) record ID of the user who either selects a medication alternative or keeps the original one in Patient Estimates. |
| 6 | `UAC_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `UAC_SEL_ALT_YN` | VARCHAR |  | Store whether user selects alternative medication from this LME. |
| 8 | `UAC_INS_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant (date and time in UTC) a user selected an alternative medication from this LME. |
| 9 | `UAC_LME_ID` | NUMERIC |  | Stores the LME .1 (record ID) of the LME record containing the selected alternative. |
| 10 | `UAC_LME_CSN` | NUMERIC |  | Stores the contact serial number (CSN) of the LME record containing the selected alternative. |
| 11 | `UAC_LME_LN_NUM` | INTEGER |  | Stores the line number containing the selected alternative in superitem LME 300 of the alternative LME record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MED_ESTIMATE_ID` | [MED_CVG_INFO](MED_CVG_INFO.md) | sole_pk | high |

