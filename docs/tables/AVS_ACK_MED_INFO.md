# AVS_ACK_MED_INFO

> This table contains data regarding when a user acknowledges that the medications instructions for the after visit summary are still valid if the medication list changed since the instructions were last edited.

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
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `AVS_ACK_MED_USER_ID` | VARCHAR |  | The unique ID associated with the user who acknowledged that the medication instructions in the after visit summary are still correct after the discharge medication list has changed since the instructions were last edited. |
| 7 | `AVS_ACK_MED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `AVS_ACK_MED_DTTM` | DATETIME (UTC) |  | This item contains the UTC instant at which a user acknowledged that the medication instructions in the after visit summary are still correct after the discharge medication list has changed since the instructions were last edited. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

