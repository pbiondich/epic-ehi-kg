# POC_EVENTS

> This table contains event information for the Plan of Care (POC) master file.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the plan of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `POC_EVENTS_C_NAME` | VARCHAR |  | This item contains events related to creation, modification, and filing of a POC. |
| 4 | `POC_EVENT_INST_DTTM` | DATETIME (Local) |  | This item contains the POC event instant. |
| 5 | `POC_EVENT_USER_ID` | VARCHAR |  | The unique identifier for user record associated with the plan of care event. |
| 6 | `POC_EVENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `POC_EVENT_LINK_CSN` | NUMERIC |  | The contact serial number of the plan of care contact that is linked to an event in the POC. |
| 8 | `EVENT_AUD_PREV_VAL` | VARCHAR |  | As part of audit information for events on the plan of care, this item stores the changed value for items in the POC that changed in the event. |
| 9 | `EVENT_AUD_CUR_VAL` | VARCHAR |  | As part of audit information for events on the plan of care, this item stores the original value for items in the POC that changed in the event. |
| 10 | `EVENT_AUD_HX_ITEM` | VARCHAR |  | As part of audit information for events on the plan of care, this item stores items in the POC that changed in the event. |
| 11 | `POC_EVENT_COMMENT` | VARCHAR |  | Contains the comment linked to an event in the POC events log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

