# DP_COMM_IDENTIFIER_RM

> This table contains a row for each communication that was sent from the Continued Care and Services Coordination workflow and extracts the unique identifier of each communication.

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
| 7 | `COMM_IDENTIFIER` | INTEGER |  | Unique identifier for a communication sent from CCSC. Together with the PAT_ENC_CSN_ID column, this forms the foreign key to the DP_COMM_ATTACHMENTS table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

