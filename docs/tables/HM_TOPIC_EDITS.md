# HM_TOPIC_EDITS

> The HM_TOPIC_EDITS table includes all Health Maintenance topics that have overridden information specific to this patient. For example, a user may specify a frequency to use for a given patient instead of the defaults coming from the Health Maintenance topic or Health Maintenance plan records.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HM_EDIT_TOPIC_ID` | NUMERIC |  | This item contains all of the Health Maintenance Topics that this patient has edits for. Any edits to a topic for a patient will supersede the automatic defaults from the HMT or HMP record. |
| 4 | `HM_EDIT_TOPIC_ID_NAME` | VARCHAR |  | The name of the health maintenance topic. |
| 5 | `HM_EDIT_FREQ` | VARCHAR |  | This item contains the edited frequency for a given Health Maintenance topic for this patient. Any edits to a topic for a patient will supersede the automatic defaults from the HMT or HMP record. |
| 6 | `HM_EDIT_RSN_C_NAME` | VARCHAR | org | This item contains the reasons for each edited frequency of an HM Topic for this patient. |
| 7 | `HM_EDIT_CMT` | VARCHAR |  | This item contains comments for each edited frequency of an HM Topic for this patient. |
| 8 | `HM_EDIT_RECOM_ID` | NUMERIC |  | This item contains the Recommendation record ID that is driving the associated Health Maintenance Topic patient specific frequency. |
| 9 | `HM_EDIT_DUE_DATE` | DATETIME |  | This item contains the specified due date of the associated Health Maintenance Topic. This due date will supersede any due date calculated from the patient specific frequency. |
| 10 | `HM_EDIT_MSG_ID` | VARCHAR |  | This item contains the In Basket message record ID that is driving the associated Health Maintenance topic patient specific frequency. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

