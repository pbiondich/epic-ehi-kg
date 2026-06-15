# DENTAL_PROCEDURE_HX

> This table contains the history of edits for dental procedure records.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 33  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DENTAL_PATIENT_CSN` | NUMERIC |  | Stores the patient encounter in which a particular contact of the record was modified if it was available. |
| 4 | `DENTAL_MOD_USER_ID` | VARCHAR |  | Stores the user who modified the procedure record. |
| 5 | `DENTAL_MOD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `DENTAL_MOD_INSTANT_DTTM` | DATETIME (Attached) |  | Stores the date and time when dental procedure record was modified. |
| 7 | `DENTAL_ARCH_HIST_C_NAME` | VARCHAR |  | Stores the revision history of the arch for a procedure. |
| 8 | `DENTAL_QUAD_HIST_C_NAME` | VARCHAR |  | Stores the revision history of the quadrant for a procedure. |
| 9 | `DENTAL_EAP_HIST_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 10 | `DENT_COMP_INST_HIST_DTTM` | DATETIME (Attached) |  | Stores the revision history of when a procedure is completed |
| 11 | `PROC_STAT_HIST_C_NAME` | VARCHAR |  | This column keeps track of how status of a procedure changes over time. |
| 12 | `DENT_VISIT_HIST_ID` | NUMERIC |  | This column keeps track of the visit that contains the procedure over time. |
| 13 | `DENT_CHRON_INSTANT_DTTM` | DATETIME (Attached) |  | This is the date and time the documentation was made for, such as when documenting past historical data. |
| 14 | `DENTAL_COMP_PROV_HX_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 15 | `DENT_TTH_AREA_HX_C_NAME` | VARCHAR |  | This determines the history of the part of the tooth that a procedure or finding affects. |
| 16 | `DENT_PLN_VIS_NUM_HX` | INTEGER |  | This item stores the historical values of the planned visit for a procedure. |
| 17 | `DENTAL_B_PROV_HX_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 18 | `DENT_PLAN_PRL_HX_ID` | NUMERIC |  | History of the treatment template to be used when the user creates a treatment plan for the dental procedure |
| 19 | `DENT_PLAN_PRL_HX_ID_PROTOCOL_NAME` | VARCHAR |  | The SmartSet/Protocol record name. This is different from the display name, which is stored in CL_PRL_SS_OT.DISPLAY_NAME. |
| 20 | `DENT_RMV_RSN_HX_C_NAME` | VARCHAR | org | The history of the reason an existing procedure was removed from a patient's tooth chart. |
| 21 | `DENT_PROC_HX_IMP_ID` | VARCHAR |  | This item stores the implant record ID historically linked to a dental procedure. |
| 22 | `DENTAL_AREA_HIST_C_NAME` | VARCHAR |  | History of the area of the oral cavity that a dental procedure is performed on. |
| 23 | `DENTAL_ORD_HX_ID` | NUMERIC |  | This column contains the history of the linked order record for a dental procedure. |
| 24 | `DENTAL_PROC_NOTE_HX_ID` | VARCHAR |  | Historical ID of the note (HNO) record that served as this dental procedure's Completion Details note |
| 25 | `DENT_TRIG_PROC_HX_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 26 | `LINKED_BRIDGE_PROC_HX` | NUMERIC |  | Linked bridge ID history for a bridge procedure |
| 27 | `DENT_PROC_SUBSTATUS_C_NAME` | VARCHAR | org | This item keeps track of how the substatus of a procedure changes over time. This is the category ID. |
| 28 | `DENT_AREA_INACTV_HX_YN` | VARCHAR |  | Tracks the audit history of whether a non-teeth procedure should be considered inactive. |
| 29 | `DENT_MOD_APPROVAL_USER_ID` | VARCHAR |  | The user that approved a modification to a previously-approved procedure |
| 30 | `DENT_MOD_APPROVAL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 31 | `DENT_PROC_HX_DNF_ID` | NUMERIC |  | The linked procedure (RES) ID that was marked Did Not Finish, to be completed in a subsequent visit |
| 32 | `DENT_REPL_PROSTH_HX_YN` | VARCHAR |  | This item stores the history of whether or not the dental procedure is a replacement prosthesis. |
| 33 | `REPL_PROSTH_PLAC_DATE` | DATETIME |  | This item stores the history of the date of prior placement of a prosthesis procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

