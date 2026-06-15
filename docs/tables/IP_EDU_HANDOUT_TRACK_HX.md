# IP_EDU_HANDOUT_TRACK_HX

> Stores a history of all education patient materials marked as given or viewed by the patient.

**Primary key:** `PED_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PED_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the education record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `HANDOUT_LINK_HX` | VARCHAR |  | Stores the handout link history for all patient handouts received by the patient. |
| 6 | `HANDOUT_NAME_HX` | VARCHAR |  | The handout name history for all patient handouts received. |
| 7 | `GIVEN_HX_USER_ID` | VARCHAR |  | Stores the user ID for all handouts that have been directly marked as given to the patient. |
| 8 | `GIVEN_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `VIEWED_HX_MYPT_ID` | VARCHAR |  | Stores the history of all MyChart accounts that viewed the patient material. |
| 10 | `RECEVD_HX_INST_DTTM` | DATETIME (Local) |  | The instant history for any patient material that was received by the patient. |
| 11 | `SMARTTEXT_ID` | VARCHAR | FK→ | The ETX ID history for all clinical references that have been viewed by the patient. |
| 12 | `SMARTTEXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 13 | `FDI_HX_CLIENT_IDENT` | VARCHAR |  | Stores the history of FDI Client IDs for all FDI handouts received by the patient |
| 14 | `DELETED_YN` | VARCHAR |  | Whether this handout has been marked as given or if the given status has been deleted. |
| 15 | `HANDOUT_MAX_PROGRESS_HX` | INTEGER |  | Stores the max progress history in seconds of the video/audio handouts viewed by patient or proxies. |
| 16 | `HANDOUT_DURATION_HX` | INTEGER |  | Stores the duration history in seconds of the video/audio handouts assigned to patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PED_ID` | [CL_PAT_EDU_NS](CL_PAT_EDU_NS.md) | sole_pk | high |
| `SMARTTEXT_ID` | [SMARTTEXT](SMARTTEXT.md) | sole_pk | high |

