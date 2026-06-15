# CMGMT_REV_ENC_EPSD_UPDT

> Stores details about outreach encounters that are linked to one or more Case Management episodes. The CMGMT_* columns store information related to reviewing the case management episodes.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CMGMT_EPISODE_ID` | NUMERIC |  | Stores the unique identifier for the case episode which this encounter is reviewing. |
| 5 | `CMGMT_EPISODE_REVIEWED_YN` | VARCHAR |  | Indicates whether the associated case team line has completed their review of the linked case episode. |
| 6 | `CMGMT_EPISODE_CASE_TEAM_LINE` | INTEGER |  | Store the line number corresponding to a linked case episode's case team line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

