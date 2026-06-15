# DOCS_RCVD_DX

> This table stores discrete diagnosis information received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 26  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `DX_REF_ID` | VARCHAR |  | Reference ID for this diagnosis. |
| 6 | `DX_ENC_ID` | VARCHAR |  | Reference ID of the encounter associated with this diagnosis. |
| 7 | `DX_NAME` | VARCHAR |  | Display name of this diagnosis. |
| 8 | `DX_CONTEXT_C_NAME` | VARCHAR |  | The type of diagnosis. |
| 9 | `DX_SRC_CSN` | NUMERIC |  | Contains the Contact Serial Number (CSN) of the source external document record that has the external diagnosis information. |
| 10 | `DX_START_DTTM` | DATETIME (Local) |  | Start time for this diagnosis. |
| 11 | `DX_END_DTTM` | DATETIME (Local) |  | End time for this diagnosis. |
| 12 | `DX_EDG_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 13 | `DX_LST_UPD_INST_DTTM` | DATETIME (UTC) |  | Stores the last update instant of the diagnosis in UTC. |
| 14 | `DX_PRIMARY_YN` | VARCHAR |  | Denotes if this diagnosis is the primary diagnosis. |
| 15 | `DX_FILTER_RSN_C_NAME` | VARCHAR |  | Stores the reason why an external diagnosis should be filtered from the composite external document record |
| 16 | `DX_IS_ED_YN` | VARCHAR |  | Denotes if this diagnosis was made in the ED. |
| 17 | `DX_BULK_STAT_C_NAME` | VARCHAR |  | The status of this data element within DINE. |
| 18 | `DX_BULK_INCL_DATE` | DATETIME |  | The date to compare to the change tracking window when loading flat files in bulk via DINE. If the date is within the window, but the data element is missing from the load, then the data element is invalidated. |
| 19 | `DX_GENERIC_NAME` | VARCHAR |  | The generic name for an Ambient-detected dianosis, representing what was heard in the visit recording. |
| 20 | `DX_BEST_MATCH_DX_REFID` | VARCHAR |  | For an Ambient diagnosis, stores the ID from I DXR 11300 of the Ambient diagnosis that this is an alternative to. This allows Ambient vendors to send multiple variations of a single detected diagnosis for a provider to choose from. |
| 21 | `DX_CONFIDENCE_RANK` | INTEGER |  | Ranking of confidence in an Ambient-detected diagnosis, compared to other alternatives presented, with 1 being the most confident. |
| 22 | `DX_STATE_HOLOGRAM_ID` | NUMERIC |  | ID of the HOL record storing the current state of an Ambient-detected diagnosis |
| 23 | `DX_TOPIC_NAME` | VARCHAR |  | The topic name for an Ambient-detected diagnosis. Diagnoses that share a topic name will be grouped together under that name when presented to the user in the "Heard In Visit Recording" workflow. |
| 24 | `DX_NOTED_DATE` | DATETIME |  | This item stores the noted date for the visit diagnosis from a hospital admission, which comes from the hospital problem list. |
| 25 | `DX_DOCUMENTED_INST_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant the diagnosis was first documented in UTC. |
| 26 | `DX_POA_C_NAME` | VARCHAR | org | This item stores the present on admission category value for the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

