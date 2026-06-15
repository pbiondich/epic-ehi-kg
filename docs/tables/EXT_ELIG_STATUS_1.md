# EXT_ELIG_STATUS_1

> This table contains the query line results from external eligibility queries to RxHub. Related external eligibility information is stored in the EXT_ELIG_STATUS table.

**Overflow of:** [EXT_ELIG_STATUS](EXT_ELIG_STATUS.md)  
**Primary key:** `PAT_ENC_CSN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated external eligibility query in this query contact. Together with PAT_ENC_CSN_ID, this forms the foreign key to the EXT_ELIG_STATUS table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple external formulary queue lines that are associated with the external eligibility query from the EXT_ELIG_STATUS table. |
| 4 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 5 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 6 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 7 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 8 | `EXT_FORM_Q_LINE` | INTEGER |  | This column contains the external formulary query line information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

