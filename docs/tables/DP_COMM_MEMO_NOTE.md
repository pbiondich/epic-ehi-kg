# DP_COMM_MEMO_NOTE

> This table contains the Free Text Note(HNO) IDs of communications sent to a service through the Continued Care and Services Coordination workflow, along with the patient CSN, patient ID, and contact date of the associated encounter. There is one line per communication sent.

**Primary key:** `PAT_ENC_CSN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated post-acute service provider in the patient encounter considered for the patient's post-acute care. Together with the PAT_ENC_CSN_ID column, this forms the foreign key to the DP_FACILITY table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple communications sent from the Continued Care and Services Coordination navigator section that are associated with the patient encounter and post-acute facility from the DP_FACILITY table. |
| 4 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 7 | `COMM_MEMO_NOTE_ID` | VARCHAR |  | This column is the note ID of a note containing user comments about the related communication sent to the service provider. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

