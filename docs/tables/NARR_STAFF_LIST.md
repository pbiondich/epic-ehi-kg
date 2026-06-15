# NARR_STAFF_LIST

> Staff event tracking items.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 19  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `NARR_STAFF_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `NARR_STAFF_UNK_ID` | VARCHAR |  | Stores the unique ID that is given to an unknown provider involved with an intervention until it is linked to an existing provider record. |
| 7 | `NARR_STAFF_ROLE_C_NAME` | VARCHAR | org | Stores the provider capacity (e.g. attending, resident, etc.) during this intervention. |
| 8 | `NARR_STAFF_EVENT_C_NAME` | VARCHAR | org | Indicates which type of event has been filed, for example whether a staff member has arrived or departed. |
| 9 | `NARR_STAFF_INST_TM` | DATETIME (Local) |  | The instant at which the staff event is filed. |
| 10 | `NARR_STAFF_COMMENT` | VARCHAR |  | The user-entered comment for a staff related event (i.e. marking a provider as paged or arrived). |
| 11 | `NARR_STAFF_LINKTO` | NUMERIC |  | Stores the line ID of a different event, if this event was modified or deleted by it. |
| 12 | `NARR_STF_MODINST_TM` | DATETIME (Local) |  | Stores the instant of an event's modification or deletion, if applicable. |
| 13 | `NARR_STAFF_DOCU_ID` | VARCHAR |  | The unique ID of the user who documented this event. |
| 14 | `NARR_STAFF_DOCU_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `NARR_STAFF_IS_AT_YN` | VARCHAR |  | Stores whether or not the specified staff member is marked as an attending physician. |
| 16 | `NARR_STAFF_TYPE_ID_TANK_NAME` | VARCHAR |  | The name of the tank record. |
| 17 | `NARR_STAFF_IEV_ID` | VARCHAR |  | Stores the ID of the event that has updated this event. |
| 18 | `NARR_STAFF_IEV_LINE` | INTEGER |  | Indicates that this event has been updated by another event and links to that event's line. |
| 19 | `NARR_STAFF_DOC_SRC_C_NAME` | VARCHAR |  | Stores the source of the staff documentation event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

