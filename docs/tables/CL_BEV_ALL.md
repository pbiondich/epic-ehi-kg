# CL_BEV_ALL

> This table holds the no-add, single-response items from the Bed Events (BEV) master file.

**Primary key:** `RECORD_ID`  
**Columns:** 21  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique ID of the bed event record. |
| 2 | `EVENT_TYPE_C_NAME` | VARCHAR |  | The bed event type category number for this bed event. |
| 3 | `EVENT_SOURCE_C_NAME` | VARCHAR | org | The bed event source category number for this bed event. |
| 4 | `BED_ID` | VARCHAR |  | The unique ID of the bed that this bed event pertains to. |
| 5 | `BED_ID_BED_LABEL` | VARCHAR |  | The name of the bed. |
| 6 | `EAF_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 7 | `PRIORITY_C_NAME` | VARCHAR |  | The priority category number for the bed event. |
| 8 | `DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 9 | `EPT_ID` | VARCHAR |  | The unique ID of the patient that was associated with this bed event. |
| 10 | `EPT_CSN` | NUMERIC |  | The unique contact serial number of the patient encounter that was associated with this bed event. |
| 11 | `REASN_BED_NT_ASGN_C_NAME` | VARCHAR |  | The reason not assigned category number for the bed event (if applicable). This item is cleared when the bed is assigned for cleaning. |
| 12 | `RECORD_CREATION_DT` | DATETIME |  | The date when this record was created. |
| 13 | `CANCEL_USER_ID` | VARCHAR |  | The unique ID of the user record for the user who canceled this bed event. This column is only populated for events that have been canceled. |
| 14 | `CANCEL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `CANCEL_EVENT_TM` | DATETIME (Local) |  | The instant when the bed event was canceled. This column is only populated for events that have been canceled. |
| 16 | `ADHOC_USER_ID` | VARCHAR |  | The unique ID of the user record for the user who created this bed event. This column is only populated for cleaning requests that weren't created automatically. |
| 17 | `ADHOC_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 18 | `LINKED_EVENT_ID` | NUMERIC |  | The unique ID of the Admission, Transfer, Discharge, or Leave of Absence (ADT) event that is associated with this bed event. |
| 19 | `BED_TYPE_C_NAME` | VARCHAR | org | This item tracks the bed type for the bed associated with the bed event record. |
| 20 | `PREV_OUT_EVENT_ID` | NUMERIC |  | The unique ID of the previous outgoing event of type Discharge, Transfer Out or LOA Out. If the previous event on the bed is of type incoming (Admission, Transfer In, LOA Return) instead of an outgoing type, then this item will be empty. |
| 21 | `NEXT_IN_EVENT_ID` | NUMERIC |  | The unique ID of the next incoming event of type Admission, Transfer In, or LOA Return. If the next event on the bed is of type outgoing (Discharge, Transfer Out, LOA Out) instead of an incoming type, then this item will be empty. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

