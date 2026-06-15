# IMM_ADMIN

> The IMM_ADMIN table contains information about the immunization administered. The rows included in this table are items from DXR (Document) masterfile which include information on type of immunization, administration date, administered dose, administration route, administration site, immunization manufacturer, immunization lot number, administered by, visit date, deferral reason, administration notes, administration location, administration status, administered amount, administered unit, contact serial number of the DXR record that owns the immunization instance and a unique reference identifier to identify a specific instance of an immunization.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 57  
**Org-specific columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `IMM_TYPE_ID` | NUMERIC |  | External immunization type ID. |
| 6 | `IMM_TYPE_ID_NAME` | VARCHAR |  | The name of the immunization. |
| 7 | `IMM_TYPE_FREE_TEXT` | VARCHAR |  | The immunization type information for the administered immunization as free text. |
| 8 | `IMM_DATE` | DATETIME |  | The immunization administration date. |
| 9 | `IMM_DOSE` | VARCHAR |  | The dose of immunization administered. |
| 10 | `IMM_ROUTE_C_NAME` | VARCHAR | org | The immunization administration route category ID. |
| 11 | `IMM_ROUTE_FREE_TXT` | VARCHAR |  | The immunization route information for the administered immunization as free text. |
| 12 | `IMM_SITE_C_NAME` | VARCHAR | org | The immunization administration site category ID. |
| 13 | `IMM_SITE_FREE_TXT` | VARCHAR |  | The immunization site information for the administered immunization as free text. |
| 14 | `IMM_MANUFACTURER_C_NAME` | VARCHAR | org | The immunization administered manufacturer category ID. |
| 15 | `IMM_MANUF_FREE_TEXT` | VARCHAR |  | The immunization manufacturer information for the administered immunization as free text. |
| 16 | `IMM_LOT_NUMBER` | VARCHAR |  | The immunization administered lot number. |
| 17 | `IMM_GIVEN_BY_ID` | VARCHAR |  | The immunization administering user ID. This column is frequently used to link to the table CLARITY_EMP. |
| 18 | `IMM_GIVEN_BY_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 19 | `IMM_GIVEN_BY_FT` | VARCHAR |  | The immunization given by information for the administered immunization as free text. |
| 20 | `IMM_VIS_PUB_DATE` | DATETIME |  | The immunization visit date presented to patient for the administered immunization. |
| 21 | `IMM_VIS_DATE` | VARCHAR |  | The immunization visit date for the administered immunization. |
| 22 | `IMM_DEF_RSN_FREE_TX` | VARCHAR |  | The immunization administration deferral reason as free text. |
| 23 | `IMM_DEF_REASON_C_NAME` | VARCHAR | org | The immunization administration deferral reason category ID. |
| 24 | `IMM_NOTES_RAW_DATA` | VARCHAR |  | Free text immunization notes from the immunization administration. |
| 25 | `IMM_NOTES` | VARCHAR |  | The immunization administration notes. |
| 26 | `IMM_LOCATION` | VARCHAR |  | The immunization administration location. |
| 27 | `IMM_STATUS_C_NAME` | VARCHAR |  | Status of the vaccination administration. |
| 28 | `IMM_DOSE_AMOUNT` | NUMERIC |  | Immunization dose amount. |
| 29 | `IMM_DOSE_UNIT_C_NAME` | VARCHAR | org | Immunization dose unit. |
| 30 | `IMM_SRC_DXR_CSN` | NUMERIC |  | The contact serial number of the received document record that owns the instance of this immunization. |
| 31 | `IMM_REFERENCE_ID` | VARCHAR |  | This item stores a unique reference identifier to identify a specific instance of an immunization. |
| 32 | `IMM_SCHED_ID_FT` | VARCHAR |  | Immunization schedule ID used for the administered vaccination. |
| 33 | `IMM_SCHED_NAME_FT` | VARCHAR |  | Immunization schedule name used for the administered vaccination. |
| 34 | `IMM_SCHED_CODING_FT` | VARCHAR |  | Immunization schedule coding system used for the administered vaccination. |
| 35 | `IMM_SCHED_VALID_YN` | VARCHAR |  | Whether or not the administered dose was valid for the given schedule. |
| 36 | `IMM_VALID_RSN_C_NAME` | VARCHAR | org | Description of why the given administration is valid or invalid based on its immunization schedule. |
| 37 | `IMM_VALID_RSN_FT` | VARCHAR |  | Description of why the given administration is valid or invalid based on its immunization schedule. |
| 38 | `IMM_LST_UPD_INST_DTTM` | DATETIME (UTC) |  | Stores the last update instant of the immunization in UTC. |
| 39 | `IMMNZTN_SRC_APPL_C_NAME` | VARCHAR | org | If this immunization is patient-entered, this item stores the application the patient used to edit the immunization for the contact (MyChart or Welcome). If this item is blank, it is assumed that the patient edited the immunization in MyChart. |
| 40 | `IMMNZTN_SRC_WPR_ID` | VARCHAR |  | Stores the WPR ID of the MyChart user who edited the immunization for the contact. |
| 41 | `IMM_EVENT_IDENT` | VARCHAR |  | This item stores the ID of the event that is associated with an immunization. In cases where there are multiple encounters that link to an immunization, the earliest encounter is represented here. |
| 42 | `IMM_FUNDING_SOURCE_C_NAME` | VARCHAR | org | The category ID for the funding source of the administered vaccine. |
| 43 | `IMM_VFC_ELIGIBILITY_STATUS_C_NAME` | VARCHAR | org | The category ID of the funding program that should pay for an administered vaccine. |
| 44 | `IMM_DUP_INT_IMM_ID` | NUMERIC |  | Link to an internal immunization |
| 45 | `IMM_DEFER_DUR_C_NAME` | VARCHAR | org | The vaccine administration deferral duration category ID for the vaccine administration in the received document. |
| 46 | `IMM_PRODUCT_C_NAME` | VARCHAR | org | The vaccine administration brand name category ID for the vaccine administration in the received document. |
| 47 | `IMM_PRODUCT_FT` | VARCHAR |  | The vaccine administration brand name for the vaccine administration in the received document. |
| 48 | `IMM_EXT_ADMIN_C_NAME` | VARCHAR | org | The source of information category ID for the vaccine administration in the received document. |
| 49 | `IMM_FILTER_RSN_C_NAME` | VARCHAR |  | Stores the reason why an external immunization should be filtered from the composite record |
| 50 | `IMM_RSN_FOR_VAC_C_NAME` | VARCHAR | org | Stores reason for vaccination values. |
| 51 | `IMM_EXTERNAL_IDENTIFIER` | VARCHAR |  | External ID of the immunization record. |
| 52 | `IMM_GENERATED_SERIAL_NUM` | INTEGER |  | This item stores the serial number that is generated when receiving the document. |
| 53 | `IMM_RECORDED_BY_ADMIN_YN` | VARCHAR |  | Flag indicating if this immunization was originally recorded by the organization administering it. |
| 54 | `IMM_BULK_STAT_C_NAME` | VARCHAR |  | The status of this data element within DINE. |
| 55 | `IMM_BULK_INCL_DATE` | DATETIME |  | The date to compare to the change tracking window when loading flat files in bulk via DINE. If the date is within the window, but the data element is missing from the load, then the data element is invalidated. |
| 56 | `IMM_STATUS_CODE_C_NAME` | VARCHAR |  | The HL7 Act Status code sent with an immunization in a C-CDA document, implying whether the immunization should persist in the composite and deduplicated DXR records. |
| 57 | `IMM_ADMIN_EXPIRATION_DATE` | DATETIME |  | This item contains the expiration date sent with an immunization in a C-CDA document. It is used to indicate whether the administered immunization should be considered valid or not. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

