# RT_CNCT_LAST_UPDATE_INFO

> Clarity table for ERT last update information, including internal version ID (I ERT 5100), internal last update instatn (I ERT 5101), and external last update instant (I ERT 5102).

**Primary key:** `RT_SUMMARY_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RT_SUMMARY_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the radiotherapy summary record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `INT_LAST_UPDATE_VERSION_NUM` | INTEGER |  | Stores the version ID of the most recent version of the contact. This version is incremented each time the contact receives an update through FHIR. For example, when an ERT contact is initially created, this item will be set to 1. For each subsequent update to this contact, the value in this item will be incremented by 1. This value populates the Meta.versionId element in the outgoing Procedure and ServiceRequest FHIR resources for radiotherapy summaries. |
| 6 | `INT_LAST_UPDATE_VER_UTC_DTTM` | DATETIME (UTC) |  | This item stores the last update instant of the contact, which is the instant when the version in ERT 5100 was filed. |
| 7 | `EXT_LAST_UPDATE_VERSION_DTTM` | DATETIME (Attached) |  | This item stores the last update instant of the resource that this contact corresponds to, which is the instant when the external system last updated the contents of the resource, not necessarily the instant when the contact was upated in Chronicles. This value comes from the Meta.lastUpdated element in the incoming Procedure or ServiceRequest FHIR resource. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

