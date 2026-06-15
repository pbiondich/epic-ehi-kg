# PAT_UTILIZATION_REVIEW

> This table contains information related to the patient utilization reviews entered during an admission.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 5 | `UR_NEXT_REVIEW_INST_DTTM` | DATETIME (UTC) |  | Stores the instant that the next utilization review is due by a case manager or UR specialist. |
| 6 | `NO_UTL_REV_NEEDED_YN` | VARCHAR |  | A yes or no flag determining whether a patient no longer requires utilization reviews during the admission (yes indicates no further reviews are needed). |
| 7 | `LAST_UTL_REV_USR_ID` | VARCHAR |  | The last user who updated patient level information related to utilization reviews. |
| 8 | `LAST_UTL_REV_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

