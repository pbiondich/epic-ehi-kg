# FIRST_CALL_AUDIT

> Audit trail for the patient's first contact provider.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 13  
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
| 6 | `FIRST_CALL_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 7 | `FIRST_CALL_USER_ID` | VARCHAR |  | This item identifies the user who was designated as the patient's first call following a change in coverage for the encounter treatment team. The item is only populated for assignments from the On-Call schedule. |
| 8 | `FIRST_CALL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `FIRST_CALL_TRTMNT_TEAM_REL_C_NAME` | VARCHAR | org | This item identifies the role of the provider who was designated as the patient's first call following a change in coverage for the encounter treatment team. |
| 10 | `FIRST_CALL_UPDATE_DTTM` | DATETIME (UTC) |  | This item identifies the update time of the provider who was designated as the patient's first call following a change in coverage for the encounter treatment team. This corresponds to the time the first call was referenced for use (by the system or display to an end user) and not necessarily the time at which the patient's first call provider's assignment was updated. |
| 11 | `FIRST_CALL_REASON_C_NAME` | VARCHAR |  | This item identifies the update reason for the provider who was designated as the patient's first call following a change in coverage for the encounter treatment team. |
| 12 | `FIRST_CALL_CHNG_USER_ID` | VARCHAR |  | This item identifies the update user for the provider who was designated as the patient's first call following a change in coverage for the encounter treatment team. |
| 13 | `FIRST_CALL_CHNG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

