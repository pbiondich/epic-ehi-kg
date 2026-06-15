# DISCHARGE_DELAYS_HX

> Holds the update history of discharge delays on a patient.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `DD_HX_INST_UTC_DTTM` | DATETIME (UTC) |  | Holds the instant of a change to discharge delays |
| 7 | `DD_HX_ACTION_C_NAME` | VARCHAR |  | The action taken |
| 8 | `DD_HX_LINE` | INTEGER |  | Holds the line of the delay being changed |
| 9 | `DD_HX_COMMENT` | VARCHAR |  | Holds the post-change comment of a delay history change |
| 10 | `DD_HX_ADD_UTC_DTTM` | DATETIME (UTC) |  | The item stores the instant when the delay was added. It will track the history of the value stored in item EPT 11021. |
| 11 | `DD_HX_RSLV_UTC_DTTM` | DATETIME (UTC) |  | The item stores the instant when the delay was resolved. It will track the history of the value stored in item EPT 11023. |
| 12 | `DD_HX_INST_LOCAL_DTTM` | DATETIME (Local) |  | Holds the local instant of a change to discharge delays |
| 13 | `DD_HX_ADD_LOCAL_DTTM` | DATETIME (Local) |  | The item stores the local instant when the delay was added. It will track the history of the value stored in item EPT 11028. |
| 14 | `DD_HX_RSLV_LOCAL_DTTM` | DATETIME (Local) |  | The item stores the local instant when the delay was resolved. It will track the history of the value stored in item EPT 11060. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

