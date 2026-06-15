# CAREPLAN_CNCT_INFO

> Information on care plan contacts and readings.

**Primary key:** `CAREPLAN_ID`, `CONTACT_DATE_REAL`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CAREPLAN_ID` | VARCHAR | PK shared | The unique identifier for the care plan record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CTCT_SERIAL_NUM` | NUMERIC |  | The contact serial number (CSN) of the contact. |
| 5 | `CONTACT_NUMBER` | VARCHAR |  | The number of the contact |
| 6 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 7 | `INST_OF_EDIT_DTTM` | DATETIME (Local) |  | The instant the reading was made. |
| 8 | `READING_TYPE_C_NAME` | VARCHAR |  | What the reading type is for this care plan reading |
| 9 | `READING_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for the patient. This column stores the patient encounter that the care plan was documented on. |
| 10 | `READING_EDIT_CAREPLAN_CSN_ID` | NUMERIC |  | The unique contact identifier for the care plan. If present, this points to the contact that was edited by this documentation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `READING_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

