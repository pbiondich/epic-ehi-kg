# SYNOPTIC_RESULT_MAIN

> This table contains synoptic information for a patient or a requisition grouper.

**Primary key:** `SYNOPTIC_ID`  
**Columns:** 14  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SYNOPTIC_ID` | NUMERIC | PK | The unique identifier for the synoptic result record. |
| 2 | `SYNOPTIC_NAME` | VARCHAR |  | The name of the synoptic result record. |
| 3 | `SPECIMEN_LIST` | VARCHAR |  | Stores a string of specimen names for this synoptic result record. |
| 4 | `REC_STATUS_C_NAME` | VARCHAR |  | The deletion status category ID for the synoptic result. |
| 5 | `SYN_EPT_PAT_ID` | VARCHAR | FK→ | The patient associated with this synoptic result. |
| 6 | `SYN_RQG_PAT_RECORD_ID` | NUMERIC |  | The requisition grouper associated with this synoptic result. |
| 7 | `SYN_SOURCE_RES_SYNOPTIC_ID` | NUMERIC |  | Pointer from an extracted synoptic result to the source synoptic result |
| 8 | `SYN_EXTRACT_ST_C_NAME` | VARCHAR |  | The status of the synoptic result extraction request |
| 9 | `SYN_RESULT_TYPE_C_NAME` | VARCHAR |  | The type of synoptic form result this record represents |
| 10 | `CALCULATED_VAL_CNT` | INTEGER |  | The number of elements on the form that were automatically calculated. |
| 11 | `CALCULATED_MAN_CNT` | INTEGER |  | The number of values on the form that were manually selected but could have been automatically calculated. |
| 12 | `REPEAT_SOURCE_SYNOPTIC_ID` | NUMERIC |  | Stores a pointer to the source synoptic result for this repeated section/question. |
| 13 | `REPEAT_SOURCE_ELMNT_CONCEPT_ID` | VARCHAR |  | Stores the ckey for the source element for this repeat section/question. |
| 14 | `REPEAT_COUNTER` | INTEGER |  | The counter to uniquely identify this repeat among other repeats for the same form. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SYN_EPT_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [SMRTDTA_ELEM_SYNOPTIC](SMRTDTA_ELEM_SYNOPTIC.md) | `SYNOPTIC_ID` | high |
| [SYN_FORMS](SYN_FORMS.md) | `SYNOPTIC_ID` | high |
| [SYN_SPECIMEN](SYN_SPECIMEN.md) | `SYNOPTIC_ID` | high |

