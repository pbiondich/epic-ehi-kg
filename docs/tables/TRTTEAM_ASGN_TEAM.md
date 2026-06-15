# TRTTEAM_ASGN_TEAM

> This table is used to extract the Assigned Via Team (I EPT 34107) item which represents the list of teams associated with each line in the treatment team.

**Primary key:** `PAT_ENC_CSN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated treatment team in this patient's contact. Together with PAT_ENC_CSN_ID, this forms the foreign key to the HSP_TRTMT_TEAM table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple treatment team members that are associated with the patient encounter and the treatment team from the HSP_TRTMT_TEAM table. |
| 4 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `ASGNING_TEAM_ID` | NUMERIC |  | The unique ID of the Provider Care Team that is associated with this line in the patient's treatment team. |
| 7 | `ASGNING_TEAM_ID_RECORD_NAME` | VARCHAR |  | The name of the record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

