# IP_EDU_HANDOUT_TRACKING

> Stores the current status for patient handouts that have been given to the patient or viewed on MyChart.

**Primary key:** `PED_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PED_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the education record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `HANDOUT_LINK` | VARCHAR |  | Stores the handout link for a patient handout that has been viewed by the patient or marked as given to the patient. |
| 6 | `HANDOUT_NAME` | VARCHAR |  | The handout name of a handout received by the patient. |
| 7 | `GIVEN_USER_ID` | VARCHAR |  | Stores the user ID who marked a patient handout as given. |
| 8 | `GIVEN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `VIEWED_MYPT_ID` | VARCHAR |  | Stores the WPR ID for the MyChart account that viewed the patient material. |
| 10 | `GIVEN_DTTM` | DATETIME (Local) |  | The local instant that the handout was marked as given to the patient |
| 11 | `SMARTTEXT_ID` | VARCHAR | FK→ | The ETX ID for a clinical reference that has been viewed by the patient. |
| 12 | `SMARTTEXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 13 | `FDI_DOCUMENT_IDENT` | VARCHAR |  | Stores the FDI document ID for tracking FDI handouts |
| 14 | `FDI_CLIENT_IDENT` | VARCHAR |  | Stores the client ID from the FDI patient interface for tracking FDI handouts |
| 15 | `VIEWED_DTTM` | DATETIME (Local) |  | The local instant that the material was most recently viewed by the patient electronically. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PED_ID` | [CL_PAT_EDU_NS](CL_PAT_EDU_NS.md) | sole_pk | high |
| `SMARTTEXT_ID` | [SMARTTEXT](SMARTTEXT.md) | sole_pk | high |

