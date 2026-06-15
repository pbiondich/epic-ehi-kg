# SMRTDTA_ELEM_DATA

> The SMRTDTA_ELEM_DATA table stores metadata (context, linked records, time of entry, etc.) concerning SmartData element values entered by users through SmartForms, SmartTools or other documentation tools that file discrete data to SmartData elements. The actual element values entered by end users are stored in the SMRTDTA_ELEM_VALUE table.

**Primary key:** `HLV_ID`  
**Columns:** 15  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLV_ID` | NUMERIC | PK shared | The unique ID of the SmartData element value. |
| 2 | `ELEMENT_ID` | VARCHAR | FK→ | The SmartData identifier (SDI) for this row. |
| 3 | `CUR_VALUE_DATETIME` | DATETIME (Local) |  | The date and time when the SmartData element value was entered by a user through a SmartForm, SmartTool or other documentation tool that files discrete data to SmartData elements. |
| 4 | `CUR_VALUE_USER_ID` | VARCHAR |  | The unique ID of the user who entered the SmartData element value for this row. This column is frequently used to link to the CLARITY_EMP table. |
| 5 | `CUR_VALUE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `CONTEXT_NAME` | VARCHAR |  | The name of the context associated with this row. Contexts organize SmartData element data into different categories and determine under what circumstances data is stored. Examples of contexts include "Patient" and "Episode". |
| 7 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The unique contact serial number for a contact this record is linked to. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 8 | `RECORD_ID_VARCHAR` | VARCHAR |  | The unique ID of the linked record that is associated with the SmartData element value of the current row. The type of linked record (patient, order, note, etc.) is determined by the context specified in the CONTEXT_NAME column of the current row. This column will be populated with a varchar version of the numeric ID if the type is numeric. |
| 9 | `PAT_LINK_ID` | VARCHAR |  | The unique ID of the patient record linked to the SmartData element. This column is frequently used to link to the PATIENT table. |
| 10 | `SRC_NOTE_ID` | VARCHAR |  | Links to the note record that created the current value. |
| 11 | `SRC_NOTE_STATUS_C_NAME` | VARCHAR | org | The status of the source note. |
| 12 | `CUR_VAL_UTC_DTTM` | DATETIME (UTC) |  | UTC version of HLV 70 |
| 13 | `SET_BY_C_NAME` | VARCHAR |  | Stores how this value was set |
| 14 | `SET_BY_USER_ID` | VARCHAR |  | Stores by which user this value was set |
| 15 | `SET_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ELEMENT_ID` | [OR_PNDS](OR_PNDS.md) | sole_pk | high |

