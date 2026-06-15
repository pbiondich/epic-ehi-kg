# PAT_SVC_PROV_REVIEW

> The PAT_SVC_PROV_REVIEW table contains information about the patient's review of lists of post-discharge service providers sent to them by their case manager.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `REV_LIST_IDENT` | INTEGER |  | Stores the ID of the service provider list that has been reviewed. |
| 6 | `REV_USER_MYPT_ID` | VARCHAR |  | Stores the Patient Access Account (WPR) ID of the user who reviewed this list. |
| 7 | `REV_CMT` | VARCHAR |  | Stores the reviewer's comments about their review of this list. |
| 8 | `REV_LIST_DOCUMENT_ID` | VARCHAR |  | The unique ID of the DCS document record containing the patient's signed continuing care preferences. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

