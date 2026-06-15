# PATIENT_HPI_INFO

> This table is for history of present illness information that is captured for the patient within the visit info section.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `HPI_HRV_ID_REASON_VISIT_NAME` | VARCHAR |  | The name of the Reason for Visit record. |
| 4 | `HPI_ELEM_ID_QUEST_NAME` | VARCHAR |  | The name of the question record. |
| 5 | `HPI_PROMPT` | VARCHAR |  | Stores the prompt for multiple response HPI elements related to the HPI information. |
| 6 | `HPI_VALUE` | VARCHAR |  | Stores the data values for a response to an HPI element. |
| 7 | `HPI_COMMENT` | VARCHAR |  | Stores the comment related to a history of present illness (HPI) finding. |
| 8 | `HPI_USER_ID` | VARCHAR |  | Stores the user who entered the most recent HPI information. |
| 9 | `HPI_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `HPI_UPDATED_IN_DTTM` | DATETIME (Local) |  | Stores the instant of entry for the most recent HPI information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

