# AN_RELINK_INFO

> Anesthesia automatic relinking information.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number (CSN) for this contact. The number is unique across all patient encounters in any given system. If the system uses IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 5 | `AN_RELINKRESCHED_ID` | NUMERIC |  | When this appointment is rescheduled, the anesthesia record listed here will automatically be relinked to the new appointment. |
| 6 | `AN_RELINK_TYPE_C_NAME` | VARCHAR |  | Type of relinking to perform when the appointment is rescheduled. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

