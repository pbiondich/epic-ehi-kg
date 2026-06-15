# HOLOGRAM_DETAILS

> This table stores workflow-level information about documentation pieces that have been queued up and suspended during an outpatient visit.

**Primary key:** `HOLOGRAM_ID`  
**Columns:** 8  
**Org-specific columns:** 1  
**Joined by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HOLOGRAM_ID` | NUMERIC | PK | The unique identifier (.1 item) for the hologram record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this hologram. This column is frequently used to link to the PATIENT table. |
| 3 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 4 | `HOLOGRAM_STATUS_C_NAME` | VARCHAR | org | The status category ID for selections in this hologram workflow. |
| 5 | `WORKFLOW_USER_ID` | VARCHAR |  | The unique ID associated with the user who performed this workflow. This column is frequently used to link to the CLARITY_EMP table. |
| 6 | `WORKFLOW_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `WORKFLOW_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `WORKFLOW_INST_UTC_DTTM` | DATETIME (UTC) |  | The date and time when this hologram's status was set, in UTC. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (9)

| From | Column | Confidence |
|------|--------|------------|
| [HOLOGRAM_AMBIENT_DX_INFO](HOLOGRAM_AMBIENT_DX_INFO.md) | `HOLOGRAM_ID` | high |
| [HOLOGRAM_AMBIENT_FAM_HX](HOLOGRAM_AMBIENT_FAM_HX.md) | `HOLOGRAM_ID` | high |
| [HOLOGRAM_SELECTIONS](HOLOGRAM_SELECTIONS.md) | `HOLOGRAM_ID` | high |
| [HOLOGRAM_SELECTIONS_2](HOLOGRAM_SELECTIONS_2.md) | `HOLOGRAM_ID` | high |
| [HOLO_FUP_CHKOUT_TEXT](HOLO_FUP_CHKOUT_TEXT.md) | `HOLOGRAM_ID` | high |
| [HOLO_FUP_ROUTING_RECIP](HOLO_FUP_ROUTING_RECIP.md) | `HOLOGRAM_ID` | high |
| [HOLO_LEVEL_OF_SERVICE_MOD](HOLO_LEVEL_OF_SERVICE_MOD.md) | `HOLOGRAM_ID` | high |
| [HOLO_LOS_PROC_MODIFIERS](HOLO_LOS_PROC_MODIFIERS.md) | `HOLOGRAM_ID` | high |
| [HOLO_SMARTTEXT_NOTE_TXT](HOLO_SMARTTEXT_NOTE_TXT.md) | `HOLOGRAM_ID` | high |

