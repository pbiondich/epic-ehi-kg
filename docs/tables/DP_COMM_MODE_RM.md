# DP_COMM_MODE_RM

> This table contains the communication mode ID of communications sent to a service through the Continued Care and Services Coordination workflow, along with the patient contact serial number (CSN), patient ID, and contact date of the associated encounter. There is one line per communication sent.

**Primary key:** `PAT_ENC_CSN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated post-acute service provider in the patient encounter considered for the patient's post-acute care. Together with the PAT_ENC_CSN_ID column, this forms the foreign key to the DP_FACILITY table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple communications sent from the Continued Care and Services Coordination navigator section that are associated with the patient encounter and post-acute facility from the DP_FACILITY table. |
| 4 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `DP_COMM_MODE_C_NAME` | VARCHAR |  | Method by which the communication was sent |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

