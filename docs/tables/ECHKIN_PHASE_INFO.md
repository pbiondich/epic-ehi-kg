# ECHKIN_PHASE_INFO

> The ECHECKIN_PHASE_INFO table contains information about the "just in time" eCheck-In status. Each row contains information about a single phase where eCheck-In information could be asked, such as pre-arrival or post-arrival.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `ECHKIN_PHASE_C_NAME` | VARCHAR |  | A given phase for just-in-time eCheck-In, to track statuses of eCheck-In at a given point in time. When used with the rest of the items in the related group, this allows retrieving phase-based status information, such as whether a patient completed all of their pre-arrival or post-arrival tasks. |
| 7 | `ECHKIN_PHASE_STATUS_C_NAME` | VARCHAR |  | The status for a given phase of just-in-time eCheck-In. This tracks whether a patient completed all of their tasks for a given phase, such as pre-arrival or post-arrival. |
| 8 | `ECHKIN_URL_PHASE_YN` | VARCHAR |  | Whether a URL was generated for eCheck-In during a given phase for just-in-time eCheck-In. This tracks whether a "for all" workflow was available, not whether a tickler was sent manually from front desk workflows. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

