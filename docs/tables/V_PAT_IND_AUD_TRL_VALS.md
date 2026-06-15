# V_PAT_IND_AUD_TRL_VALS

> This view provides easy querying of before and after values for items changed on patient genomic indicators.

**Primary key:** `PAT_INDICATOR_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 43

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_INDICATOR_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the patient genomic indicator record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `AUDIT_TRAIL_UTC_DTTM` | DATETIME (UTC) |  | Instant of edit for changes to this patient indicator. |
| 5 | `AUDIT_TRAIL_DTTM` | DATETIME (Local) |  | Instant of edit for changes to this patient indicator in local time of the server. |
| 6 | `AUDIT_TRAIL_USER_ID` | VARCHAR |  | The unique ID of the user who made the edit tracked to the patient genomic indicator |
| 7 | `AUDIT_TRAIL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `CHANGED_DATA_ELEMENT` | VARCHAR |  | The EHI data element that was changed |
| 9 | `PREV_CHANGED_ITEM_GROUP_LINE` | INTEGER |  | The group line of the previous value of the changed element this entry represents. For changed elements that allow only a single response, this will always be 1. |
| 10 | `PREV_CHANGED_ITEM_VALUE_LINE` | INTEGER |  | The line number of one of the multiple values associated with a specific group of data within this record. |
| 11 | `PREV_STRING_VALUE` | VARCHAR |  | If the changed element stores a string value, this column holds the previous string value. |
| 12 | `PREV_NUMBER_VALUE` | FLOAT |  | If the changed element stores a numeric value, this column holds the previous numeric value. |
| 13 | `PREV_UTC_DTTM_VALUE` | DATETIME (UTC) |  | If the changed element stores a UTC date and time, this column stores the previous value. |
| 14 | `PREV_LOC_DTTM_VALUE` | DATETIME (Local) |  | If the changed element stores a date or a date and time, this column stores the previous value in system local time. |
| 15 | `PREV_GEN_INDICATOR_ID` | NUMERIC |  | The unique ID associated with the previous genomic indicator record for this row. |
| 16 | `PREV_GEN_INDICATOR_ID_RESOLVED_PAT_FRIENDLY_NAME` | VARCHAR |  | This column provides an always populated name column that prioritizes the patient friendly name and if there is none specified, falls back to the clinical name. |
| 17 | `PREV_PAT_ID` | VARCHAR | FK→ | The unique ID associated with the previous patient record for this row. |
| 18 | `PREV_NOTE_ID` | VARCHAR |  | The unique ID associated with the previous note record for this row. |
| 19 | `PREV_CREATION_SOURCE_C` | INTEGER |  | The creation source category ID for the previous creation source associated with this row |
| 20 | `PREV_ORDER_ID` | NUMERIC |  | The unique ID associated with the previous order record for this row. |
| 21 | `PREV_COMPONENT_ID` | NUMERIC |  | The unique ID associated with the previous component record for this row. |
| 22 | `PREV_COMPONENT_ID_NAME` | VARCHAR |  | The name of the component. |
| 23 | `PREV_VARIANT_ID` | NUMERIC |  | The unique ID associated with the previous discrete variant record for this row. |
| 24 | `PREV_DOCUMENT_ID` | VARCHAR |  | The unique ID associated with the previous document record for this row. |
| 25 | `PREV_PAT_GENOMICS_IND_SRC_C` | INTEGER |  | The linking source category ID for the previous creation source associated with this row |
| 26 | `NEW_CHANGED_ITEM_GROUP_LINE` | INTEGER |  | The group line of the new value of the changed element this entry represents. For changed elements that allow only a single response, this will always be 1. |
| 27 | `NEW_CHANGED_ITEM_VALUE_LINE` | INTEGER |  | The value line of the new value of the changed element this entry represents. For changed elements that allow only a single response or one set of grouping, this will always be 1. |
| 28 | `NEW_STRING_VALUE` | VARCHAR |  | If the changed element stores a string value, this column holds the new string value. |
| 29 | `NEW_NUMBER_VALUE` | FLOAT |  | If the changed element stores a numeric value, this column holds the new numeric value. |
| 30 | `NEW_UTC_DTTM_VALUE` | DATETIME (UTC) |  | If the changed element stores a UTC date and time, this column stores the updated value. |
| 31 | `NEW_LOC_DTTM_VALUE` | DATETIME (Local) |  | If the changed element stores a date or a date and time, this column stores the updated value in system local time. |
| 32 | `NEW_GEN_INDICATOR_ID` | NUMERIC |  | The unique ID associated with the new genomic indicator record for this row. |
| 33 | `NEW_GEN_INDICATOR_ID_RESOLVED_PAT_FRIENDLY_NAME` | VARCHAR |  | This column provides an always populated name column that prioritizes the patient friendly name and if there is none specified, falls back to the clinical name. |
| 34 | `NEW_PAT_ID` | VARCHAR | FK→ | The unique ID associated with the new patient record for this row. |
| 35 | `NEW_NOTE_ID` | VARCHAR |  | The unique ID associated with the new note record for this row. |
| 36 | `NEW_CREATION_SOURCE_C` | INTEGER |  | The creation source category ID for the new creation source associated with this row |
| 37 | `NEW_ORDER_ID` | NUMERIC |  | The unique ID associated with the new order record for this row. |
| 38 | `NEW_COMPONENT_ID` | NUMERIC |  | The unique ID associated with the new component record for this row. |
| 39 | `NEW_COMPONENT_ID_NAME` | VARCHAR |  | The name of the component. |
| 40 | `NEW_VARIANT_ID` | NUMERIC |  | The unique ID associated with the new discrete variant record for this row. |
| 41 | `NEW_DOCUMENT_ID` | VARCHAR |  | The unique ID associated with the new document record for this row. |
| 42 | `NEW_PAT_GENOMICS_IND_SRC_C` | INTEGER |  | The linking source category ID for the new creation source associated with this row |
| 43 | `PREV_PAT_IND_ACT_SCORE_SRC_C` | INTEGER |  | The activity score source category ID for the previous activity score source associated with this row |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `NEW_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `PAT_INDICATOR_ID` | [PAT_INDICATOR](PAT_INDICATOR.md) | sole_pk | high |
| `PREV_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

