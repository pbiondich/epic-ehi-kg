# HH_PAT_ADDEND_EDTS

> This table contains information on a Home Health contact's addenda.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONTACT_DATE_REAL` | FLOAT |  | Unique identifier for this contact for this patient. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `ADDENDUM_NUMBER` | INTEGER |  | Number for the addendum. |
| 4 | `ADDENDUM_LINE` | INTEGER |  | Line number for the addendum. |
| 5 | `ADDENDUM_VALUE` | VARCHAR |  | Value for the addendum. |
| 6 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. This column is frequently used to link to the PAT_ENC table. |
| 7 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 8 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is populated only if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

