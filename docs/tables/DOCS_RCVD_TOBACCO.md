# DOCS_RCVD_TOBACCO

> This table stores discrete tobacco use data.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 22  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `TOB_REF_IDENT` | VARCHAR |  | This item stores the unique reference identifier associated with the tobacco use information. |
| 6 | `TOB_DATA_TYPE_C_NAME` | VARCHAR |  | This item stores the type of the tobacco use information. |
| 7 | `TOB_CHECKSUM` | INTEGER |  | This item stores the checksum associated with the tobacco use information. The checksum is used to determine whether the tobacco use information has changed when an update is received. |
| 8 | `TOB_RECORDED_DATE` | DATETIME |  | This item stores the date the tobacco use information was recorded on the sending organization. |
| 9 | `TOB_START_DATE` | DATETIME |  | This item stores the start date of the tobacco use information. |
| 10 | `TOB_END_DATE` | DATETIME |  | This item stores the end date of the tobacco use information. |
| 11 | `TOB_YEARS` | NUMERIC |  | This item stores the number of years of the tobacco use information when the start and end dates are unknown. |
| 12 | `TOB_SMOKING_TOB_USE_C_NAME` | VARCHAR |  | This item stores the smoking tobacco status. |
| 13 | `TOB_SMOKELESS_TOB_U_C_NAME` | VARCHAR |  | This item stores the smokeless tobacco status. |
| 14 | `TOB_PASSIVE_SMOKE_EXPOSURE_C_NAME` | VARCHAR |  | This item stores the passive tobacco exposure status. |
| 15 | `TOB_QUESN_TYP_C_NAME` | VARCHAR | org | This item stores the type of tobacco used. |
| 16 | `TOB_CIGARETTE_PACKS_PER_DAY` | NUMERIC |  | This item stores the cigarette packs per day. |
| 17 | `TOB_CIGARETTE_PACK_YEARS` | NUMERIC |  | This item stores the total number of cigarette pack-years. |
| 18 | `TOB_SRC_DOCUMENT_CSN_ID` | NUMERIC |  | This item stores the contact serial number of the source DXR that has this tobacco use information. |
| 19 | `TOB_SINGLE_SRC_ORG_ID` | NUMERIC |  | `This item stores the source organization for tobacco use information with a single source. |
| 20 | `TOB_SINGLE_SRC_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 21 | `TOB_START_DATE_GRANULARITY` | INTEGER |  | The granularity of the tobacco start date. Can be 1 for year, 2 for month, or 3 for day. |
| 22 | `TOB_END_DATE_GRANULARITY` | INTEGER |  | The granularity of the tobacco end date. Can be 1 for year, 2 for month, or 3 for day. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

