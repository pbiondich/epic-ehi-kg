# DOCS_RCVD_SOCIAL_HX

> This table contains discrete social history items.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 21  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `SOH_REF_ID` | VARCHAR |  | This item stores the unique reference identifier associated with the social history. |
| 6 | `SOH_TYPE_ID_C_NAME` | VARCHAR |  | This item stores the type of current social history information. |
| 7 | `SOH_START_DATE` | DATETIME |  | This item stores the start date of social history information. |
| 8 | `SOH_END_DATE` | DATETIME |  | This item stores the end date of social history information. |
| 9 | `SOH_CODE_NAME` | VARCHAR |  | This item stores the name of code which is associated with social history information. |
| 10 | `SOH_SMOK_STATUS_C_NAME` | VARCHAR |  | This item stores the smoking status information within social history. |
| 11 | `SOH_TOBACCO_TYPE_C_NAME` | VARCHAR | org | This item stores the tobacco types information within social history. |
| 12 | `SOH_PREG_EDD_DATE` | DATETIME |  | This item stores the estimated date of delivery within social history. |
| 13 | `SOH_VALUE` | VARCHAR |  | This item stores the value string of social history information. |
| 14 | `SOH_SEX_ACTIVE_C_NAME` | VARCHAR |  | This item stores the sexually active status within social history. |
| 15 | `SOH_SOURCE_DXR_CSN` | NUMERIC |  | The unique contact serial number (CSN) of the received document that contains this this social history information. |
| 16 | `SOH_SMOKELESS_C_NAME` | VARCHAR |  | This item stores smokeless tobacco use information within social history. |
| 17 | `SOH_RECORDED_DATE` | DATETIME |  | This item stores the recorded date of social history information. |
| 18 | `SOH_TRAVEL_GEO_REGION_ID` | NUMERIC |  | The geographic region to which the patient has traveled associated with this social history. |
| 19 | `SOH_TRAVEL_GEO_REGION_ID_GEO_REGION_NAME` | VARCHAR |  | The record name for the geographical region record. |
| 20 | `SOH_ALC_DRINK_C_NAME` | VARCHAR | org | Stores the type of alcohol consumed for alcohol history. |
| 21 | `SOH_ALC_DRINK_PW` | VARCHAR |  | Stores the alcohol history of drinks per week. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

