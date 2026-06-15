# HH_CPLN_VISIT_SETS

> This table contains Home Health care plan visit set information entered on the Remote Client. The table contains information about the date ranges that the visit sets are scheduled for as well as their frequency.

**Primary key:** `CAREPLAN_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 23  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CAREPLAN_ID` | VARCHAR | PK shared | Unique identifier for the care plan. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 4 | `VISIT_SET_DISC_C_NAME` | VARCHAR | org | Visit set discipline category list. Links to category table ZC_DISCIPLINE. |
| 5 | `VISIT_SET_DISC_IDX` | INTEGER |  | Visit set discipline index. |
| 6 | `VISITS_PER_PERIOD` | INTEGER |  | Visit set visits per period. |
| 7 | `PERIOD_TIME_UNTS_C_NAME` | VARCHAR |  | Period time units (day, week, prn, etc.) for the visit set. Links to category table ZC_PER_TIME_UNITS. |
| 8 | `TIME_UNITS_PER_PRD` | INTEGER |  | Visit set time units per period. |
| 9 | `VISIT_SET_DURATION` | INTEGER |  | Visit set duration. |
| 10 | `VST_SER_DISCHRG_DT` | DATETIME |  | Visit series discharge date. |
| 11 | `VST_SER_CERT_PRD` | VARCHAR |  | Visit series certification period. |
| 12 | `VST_FROM_DATE` | DATETIME |  | Visit set from date. |
| 13 | `VST_TO_DATE` | DATETIME |  | Visit set to date. |
| 14 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is populated only if you use IntraConnect. |
| 15 | `VSTS_FROM_PER_PRD` | INTEGER |  | This item stores the from part of the visits range in the visit set. |
| 16 | `VS_VERBAL_ORDER_ID` | VARCHAR |  | The verbal order linked to the visit set for a specific version of that visit set. |
| 17 | `VISIT_SET_DC_DT` | DATETIME |  | This item stores the discontinued date of the visit set, which becomes the effective end date when a visit set is discontinued. |
| 18 | `VISIT_SET_MOD_LINK` | INTEGER |  | The line number of the visit set that this was modified to. The "child" visit set. |
| 19 | `VISIT_SET_COMMENT_NOTE_ID` | VARCHAR |  | The unique ID of the note record that stores the visit set comments. |
| 20 | `VS_LAST_EDIT_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant when this visit set was last edited. |
| 21 | `SCHEDULING_INSTR_NOTE_ID` | VARCHAR |  | This item stores the HNO ID for the visit set scheduling instructions. |
| 22 | `VISIT_SET_VER` | INTEGER |  | The current version of the visit set. |
| 23 | `VISIT_SET_VER_ON_POC` | INTEGER |  | The version of the visit set currently on the patient's Plan of Care. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

