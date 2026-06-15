# ED_EVENT_HISTORY

> This table contains the audit trail and history of the event record.

**Primary key:** `EVENT_ID`, `LINE`  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | VARCHAR | PK FK→ | The unique ID of the event record. |
| 2 | `LINE` | INTEGER | PK | The line number of the information associated with this event. Multiple pieces of information can be associated with this record. |
| 3 | `EVENT_LINE` | VARCHAR |  | The line number of the original recorded event. Together with the EVENT_ID column, this forms the foreign key to ED_IEV_EVENT_INFO. |
| 4 | `EVENT_EDITED_TIME` | DATETIME (Local) |  | The date and time when the event was edited. |
| 5 | `EVNT_DISP_NAME_AUD` | VARCHAR |  | The display name of the edited event. |
| 6 | `EVENT_AUDIT_TIME` | DATETIME (Local) |  | The date and time when this edited event occurred. |
| 7 | `EVT_REC_AUDIT_TIME` | DATETIME (Local) |  | The date and time when this edited event was recorded. |
| 8 | `EVT_AUDIT_USER_ID` | VARCHAR |  | The unique ID of the user who created this edited event. |
| 9 | `EVT_AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `EVT_EDITED_USER_ID` | VARCHAR |  | The unique ID of the user who edited this event. This user might not be the user who initially created this edited event. |
| 11 | `EVT_EDITED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `EVENT_CMT_AUDIT` | VARCHAR |  | The comments associated with this edited event. |
| 13 | `STAFFED_BEDS_AUDIT` | NUMERIC |  | The number of staffed beds for a department at the time of the edited event. This item is only populated if you are using the Staffed Beds activity. |
| 14 | `EVENT_AUDIT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 15 | `EVENT_STAT_AUDIT_C_NAME` | VARCHAR |  | The category number of the status of the edited event. |
| 16 | `EVENT_INI_REC_ID_A` | VARCHAR |  | The master file and ID of the source of a edited duplicate procedure alert event. For example, this item usually holds LDG-ID (the ID of the procedure duplicate group used) or EAP-ID (the ID of the procedure used). |
| 17 | `EVENT_CONTEXT_AUDIT` | VARCHAR |  | For some edited events, this column holds the context of the edited event. Lab Ordered events might store the order ID here. Duplicate procedure alert events might store information on specific user actions in response to the alert. |
| 18 | `EVENT_NOTECSN_AUDIT` | NUMERIC |  | The event note contact serial number (CSN) of the event that was edited. This can be used to determine the note content at each edit. |
| 19 | `EVENT_AUDIT_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 20 | `ED_C_CLIENT_SRC_A_C_NAME` | VARCHAR |  | The audit trail for where the ED Course comment was filed from. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |

