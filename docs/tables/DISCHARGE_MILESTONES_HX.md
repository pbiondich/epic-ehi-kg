# DISCHARGE_MILESTONES_HX

> This table contains the history of discharge milestones for a patient encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `DISCH_MILEST_UPD_HX_UTC_DTTM` | DATETIME (UTC) |  | Instant a discharge milestones event was triggered. |
| 5 | `DISCH_MILEST_AUTOMANAGED_HX_YN` | VARCHAR |  | Determines if discharge milestones have had any manual intervention at the time of the event. Discharge Milestones are considered auto-managed if the discharge order is the sole driver for kicking off and discontinuing milestones. |
| 6 | `DISCH_MILEST_EVENT_HX_C_NAME` | VARCHAR | org | History item for discharge milestone events. The possible events are Started and Canceled. Started - This event occurs when discharge milestones are initiated with the discharge order, the Start Discharge Milestones extension, or the Discharge Milestones navigator section. Canceled - This event occurs when the discharge milestones are canceled via the discharge order or the Discharge Milestones navigator section. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

