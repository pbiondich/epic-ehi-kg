# PRE_CLM_REV_SUBM_HX

> This table contains the Home Health pre-claim review submission audit history.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `EDIT_LINE` | INTEGER |  | The line number that was changed during an edit to the Pre-Claim Review. This is the line number found in column LINE of the table PRE_CLM_REV_SUBMISSIONS. |
| 5 | `PREV_VALUE` | VARCHAR |  | The value that was changed during an edit to the Pre-Claim Review submission. |
| 6 | `NEW_VAL` | VARCHAR |  | The new value entered during an edit to the Pre-Claim Review submission. |
| 7 | `EDIT_USER_ID` | VARCHAR |  | The ID of the user that performed the change during an edit to the Pre-Claim Review submission. |
| 8 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `EDIT_DTTM` | DATETIME (Local) |  | The instant at which an edit to the Pre-Claim Review submission was made. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

