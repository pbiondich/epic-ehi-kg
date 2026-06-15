# EXCUSE_TEMPLATE

> The EXCUSE_TEMPLATE table contains information about disposition workspace excuse letters generated for a patient's encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the excuse associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `EXCUSE_TEMPLATE_NAME` | VARCHAR |  | Name of the excuse template selected to print. |
| 6 | `EXCUSE_ETX_ID` | VARCHAR |  | The record ID of the SmartText (pre-defined blocks of text) that an excuse template uses to generate the letter to print. |
| 7 | `EXCUSE_ETX_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 8 | `EXCUSE_ETX_VERSION` | FLOAT |  | Specific version of the SmartText (pre-defined blocks of text) the excuse template uses to generate the letter to print. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 9 | `EXCUSE_COMMENT` | VARCHAR |  | Comment the provider entered after the excuse template to be printed as part of the excuse letter. |
| 10 | `EXCUSE_STAT_C_NAME` | VARCHAR |  | The status of the excuse |
| 11 | `COPY_FROM_LINE` | INTEGER |  | Stores a reference to the line containing the excuse that this excuse was copied from. |
| 12 | `EXCUSE_EDITOR_POS` | INTEGER |  | Stores the relative positions of pending excuses text as individual excuses are printed or deleted. |
| 13 | `EXCUSE_COMM_JOB_ID` | VARCHAR |  | Stores a pointer to the ID of the communication job (i.e. email, letter, fax) associated with the excuse. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

