# ED_IEV_PAT_INFO

> This table contains information that is useful for linking records (patient, department, etc.) to their appropriate events.

**Primary key:** `EVENT_ID`  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | VARCHAR | PK FK→ | The unique ID of the event record. This column is frequently used to link to the ED_IEV_EVENT_INFO table. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this line. This column is frequently used to link to the PATIENT table. |
| 3 | `ITEMS_EDITED_TIME` | DATETIME |  | The date and time when this event record was last edited. |
| 4 | `UPDATE_DATE` | DATETIME (Local) |  | The last date and time the event record was extracted. |
| 5 | `PAT_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 6 | `DTE_EXTERNAL` | DATETIME |  | The date of this contact in calendar format. |
| 7 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across patients and encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 8 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique, internal patient contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 9 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 10 | `DEPT_EVENT_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 11 | `RECORD_STATE_C_NAME` | VARCHAR |  | The record state category number for the event record. Link this column to the ZC_PBA_REC_STAT table to look up the corresponding record state values. |
| 12 | `TRANSFER_STATUS_C_NAME` | VARCHAR |  | The transfer status category number for medication reconciliation events. |
| 13 | `CREATE_DTTM` | DATETIME (Local) |  | The instant when the event record was created. |
| 14 | `CREATE_USER_ID` | VARCHAR |  | The unique ID of the user who created the event record. |
| 15 | `CREATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 16 | `EVENT_DATE` | DATETIME |  | The date the event record was created. |
| 17 | `PAT_CSN` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across patients and encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 18 | `ADT_TRANSFER_LINK` | INTEGER |  | Virtual item for the Admission, Transfer, Discharge, or Leave of Absence (ADT) event link for a medication reconciliation transfer. |
| 19 | `REG_CLIP_FREETEXT` | VARCHAR |  | User-entered patient name for patient added to clipboard. User-entered text is necessary for users without security to select real patients or for new patients. |
| 20 | `REG_CLIP_COMMENTS` | VARCHAR |  | Comments for the patient added to the Patients Waiting Registration Clipboard |
| 21 | `IP_ORDREC_SORT_DTTM` | DATETIME (Local) |  | This is the instant that all the orders in the event should be sorted by, instead of using their individual ordering session keys or ordering instants. |
| 22 | `REG_WAIT_STATE_C_NAME` | VARCHAR |  | Holds the state of the record that holds Registration wait list info. |
| 23 | `REG_WAIT_PAT_NAME` | VARCHAR |  | Holds the user-entered patient name for a patient who is waiting but has not yet been identified. |
| 24 | `REG_WAIT_IS_PRI_YN` | VARCHAR |  | Holds the priority value for a patient who is waiting to be registered. |
| 25 | `REG_WAIT_ARRV_DTTM` | DATETIME (Local) |  | Holds the earliest event instant, which will indicate the time the patient arrived for the encounter this event list is associated with. |
| 26 | `AVS_COPY_FORWARD_DTTM` | DATETIME (UTC) |  | The date and time that a user copied After Visit Summary documentation from another encounter into this one. |
| 27 | `AVS_COPY_FORWARD_USER_ID` | VARCHAR |  | The unique ID of the user who copied After Visit Summary documentation from another encounter into this one. |
| 28 | `AVS_COPY_FORWARD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |
| `PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

