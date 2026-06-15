# DP_SVC_COORD_NOTE

> Coordination notes from the Services to Coordinate section of the current patient encounter--used to leave care coordination notes specific to this patient to a user, or to other users coordinating care for the patient.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `COORD_NOTE_ID` | VARCHAR |  | Contains the HNO (unified clinical notes master file) IDs of any coordination notes that have been created for the current patient encounter. Coordination notes exist to document any additional context surrounding current service coordination plans that cannot be documented in the plan itself. |
| 7 | `NOTE_IS_PINNED_YN` | VARCHAR |  | Matches with an HNO ID stored in I EPT 97118, and documents if that coordination note is "pinned." Pinned coordination notes will show up in the Services to Coordinate navigator section, and any users accessing that patient's chart will be able to see that note during service coordination. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

