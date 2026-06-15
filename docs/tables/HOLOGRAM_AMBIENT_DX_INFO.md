# HOLOGRAM_AMBIENT_DX_INFO

> This table contains information about the Ambient diagnosis choices that were presented to a clinician.

**Primary key:** `HOLOGRAM_ID`, `CONTACT_DATE_REAL`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HOLOGRAM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the hologram record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. For Hologram, the contact date is irrelevant. For the workflow timestamp, use the WORKFLOW_INST_UTC_DTTM column in the HOLOGRAM_DETAILS table. |
| 3 | `AMBIENT_DX_SOURCE_C_NAME` | VARCHAR |  | Stores the source from which an Ambient diagnosis option was derived. (Problem List, Visit Diagnoses, etc.) |
| 4 | `AMBIENT_DX_LNK_PROB_LST_ID` | NUMERIC |  | Stores the ID of the problem associated with this Ambient diagnosis selection. |
| 5 | `AMBIENT_DX_LINKED_VDX` | VARCHAR |  | Stores the ID of the visit diagnosis that this Ambient diagnosis option was derived from. If this diagnosis came from a past encounter, the CSN of that encounter is stored in the AMBIENT_PAST_DX_CSN column. |
| 6 | `AMBIENT_DX_AUTO_MATCH_YN` | VARCHAR |  | Stores whether or not an existing diagnosis was automatically matched to the Ambient diagnosis. |
| 7 | `ADD_DX_TO_PROBLIST_YN` | VARCHAR |  | Stores whether or not the Ambient diagnosis is marked to be pushed to the Problem List. |
| 8 | `INITIAL_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 9 | `AMBIENT_PAST_DX_CSN` | NUMERIC |  | If an Ambient diagnosis matched to a past visit diagnosis, this item stores the CSN of the patient encounter in which that visit diagnosis was documented. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HOLOGRAM_ID` | [HOLOGRAM_DETAILS](HOLOGRAM_DETAILS.md) | sole_pk | high |

