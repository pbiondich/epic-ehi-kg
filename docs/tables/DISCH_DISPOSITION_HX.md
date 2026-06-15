# DISCH_DISPOSITION_HX

> This is the discharge disposition history table. It will track the changes made to the patient's discharge disposition throughout the encounter. This table contains the data about the discharge disposition (I EPT 11100), the user that made the change (I EPT 11101), the date and time that the discharge disposition was entered (I EPT 11102), and the source of the update to discharge disposition (I EPT 11104).

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `DISCH_DISP_C_NAME` | VARCHAR | org | Stores a history of the discharge disposition. |
| 7 | `DISCH_DISP_USER_ID` | VARCHAR |  | Stores a history of users who updated the discharge disposition. |
| 8 | `DISCH_DISP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `DISCH_DISP_INST_LOCAL_DTTM` | DATETIME (Attached) |  | Stores a history of when the discharge disposition was updated. |
| 10 | `DISCH_DISP_INST_UTC_DTTM` | DATETIME (UTC) |  | Stores a history of when the discharge disposition was updated in UTC. |
| 11 | `DISCH_DISP_UPD_SOURCE_C_NAME` | VARCHAR |  | The source of a change to the discharge disposition. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

