# DOCS_RCVD_CLINICAL_NOTES

> This table contains metadata about clinical notes retrieved from external sources. Each row represents a discrete clinical note received in this document.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 35  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `NOTE_REFERENCE_IDENT` | VARCHAR |  | The reference ID of the clinical note, which uniquely identifies the note. |
| 6 | `NOTE_EXTERNAL_UNIQUE_IDENT` | VARCHAR |  | The externally-assigned globally unique identifier for the clinical note. |
| 7 | `NOTE_LOCAL_UNIQUE_IDENT` | VARCHAR |  | The locally-assigned unique identifier for the clinical note. |
| 8 | `NOTE_FHIR_DOCREF_RESRC_IDENT` | VARCHAR |  | The logical ID of the FHIR Document Reference resource for the clinical note. |
| 9 | `NOTE_FHIR_DOCREF_ATTACHT_URL` | VARCHAR |  | The URL containing the content of the clinical note. |
| 10 | `NOTE_SOURCE_ORG_ID` | NUMERIC |  | The unique ID of the organization record that represents the original source of this clinical note. |
| 11 | `NOTE_SOURCE_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 12 | `NOTE_STATUS_C_NAME` | VARCHAR | org | The current status of the clinical note. |
| 13 | `NOTE_SHARED_WITH_PAT_YN` | VARCHAR |  | Indicator of whether the clinical note was allowed to be shared with the patient at the source organization for the note. A Yes value does not imply the patient has actually viewed the note. |
| 14 | `NOTE_UCN_TYPE_C_NAME` | VARCHAR | org | The mapped type of the clinical note in the Unified Clinical Notes framework. |
| 15 | `NOTE_TYPE_NAME` | VARCHAR |  | The free-text description of the type of the clinical note. |
| 16 | `NOTE_LAST_FILED_UTC_DTTM` | DATETIME (UTC) |  | The instant the clinical note was last meaningfully modified at the note's source organization. |
| 17 | `NOTE_CREATION_UTC_DTTM` | DATETIME (UTC) |  | The instant the clinical note was originally created at the note's source organization. |
| 18 | `NOTE_LAST_SIGNED_UTC_DTTM` | DATETIME (UTC) |  | The instant the clinical note was most recently signed or co-signed. |
| 19 | `NOTE_LAST_SIGNER_NAME` | VARCHAR |  | The name of the individual that most recently signed or co-signed the clinical note. |
| 20 | `NOTE_AUTHOR_NAME` | VARCHAR |  | The name of the author of the clinical note. |
| 21 | `NOTE_AUTHOR_TYPE` | VARCHAR |  | The free-text description of the type of provider that authored the clinical note. |
| 22 | `NOTE_AUTHOR_SERVICE` | VARCHAR |  | The free-text description of the service associated with the authorship of the clinical note. |
| 23 | `NOTE_AUTHOR_SPECIALTY_C_NAME` | VARCHAR | org | The mapped provider specialty of the author of the clinical note. |
| 24 | `NOTE_AUTHOR_SPECIALTY_NAME` | VARCHAR |  | The free-text description of the provider specialty of the author of the clinical note. |
| 25 | `AUTORECONCILED_UCN_NOTE_ID` | VARCHAR |  | The unique ID of the note record automatically created in the local chart from this received clinical note. |
| 26 | `NOTE_FILTER_REASON_C_NAME` | VARCHAR |  | Stores the reason this external clinical note should be filtered and thus not auto-reconciled into the local chart. Calculated at the time the note is received and saved. |
| 27 | `NOTE_ASSOC_EVENT_IDENT` | VARCHAR |  | The reference ID of the encounter associated with the clinical note. Is associated with a value from I DXR 8010. |
| 28 | `NOTE_SERVICE_START_UTC_DTTM` | DATETIME (UTC) |  | The instant of service associated with the clinical note. |
| 29 | `NOTE_SRC_DOCREF_RESRC_IDENT` | VARCHAR |  | The ID of the FHIR Document Reference resource for the source note of the clinical note. Populated when the clinical note is an interval note. |
| 30 | `NOTE_REMOVED_YN` | VARCHAR |  | Indicates whether the note is no longer in the received note list |
| 31 | `NOTE_ASSOC_PROB_IDENT` | VARCHAR |  | The reference ID of the external problem linked to a clinical note. |
| 32 | `NOTE_AUTHOR_TYPE_C_NAME` | VARCHAR | org | The internal category value of the type of provider that authored the clinical note. |
| 33 | `NOTE_SRC_DXR_CSN` | NUMERIC |  | This item will store the contact serial number of the DXR record that owns the instance of this note. |
| 34 | `NON_UCN_NOTE_TEXT_HNO_NOTE_ID` | VARCHAR |  | The ID of the note record that store the text from a note received for Professional Billing Exchange |
| 35 | `NOTE_AUTHOR_NPI` | VARCHAR |  | The National Provider Identifier for the provider that authored the clinical note. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

