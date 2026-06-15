# PAT_ENC_CHART_REV

> This table contains information about who reviewed a patient chart and the instant that they reviewed it. The patient chart is synonymous with a patient encounter or contact in this table. With appropriate setup the patient chart can be reviewed from In Basket and a chart/encounter can be reviewed more than once and by more than one person. Each instance and person that reviews a chart will be stored in this table.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CHRT_REV_BY_USER_ID` | VARCHAR |  | The unique ID associated with the user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| 6 | `CHRT_REV_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `CHRT_REV_ON_DTTM` | DATETIME (Local) |  | The instant when the patient chart was reviewed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

