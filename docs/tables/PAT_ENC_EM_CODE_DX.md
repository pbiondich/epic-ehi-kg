# PAT_ENC_EM_CODE_DX

> The PAT_ENC_EM_CODE_DX table enables you to report on the diagnoses associated with evaluation and management (E/M) codes entered for a patient encounter. Since one E/M code may be associated with multiple diagnoses, each row in this table is one E/M code - diagnosis relation. This table contains only information for those E/M codes and diagnoses that have been explicitly associated.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `EM_CODE_LINE` | INTEGER |  | The indicator of the E/M code associated with the diagnosis. This value corresponds to the LINE column in the ADDITIONAL_EM_CODE table. Together with PAT_ENC_CSN_ID, this forms the foreign key to the ADDITIONAL_EM_CODE table. |
| 6 | `DX_UNIQUE` | VARCHAR |  | The unique identifier of the diagnosis associated with the Evaluation and Management (E/M) code. This value corresponds to the DX_UNIQUE column in the PAT_ENC_DX table. Together with PAT_ENC_CSN_ID, this forms the foreign key to the PAT_ENC_DX table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

