# PAT_SVC_PROV_SEARCH_LIST

> This table stores metadata for a list of post-discharge service providers that was given to a patient so that they can indicate their preference. The service providers that are part of the list are in PAT_SVC_PROV_SEARCH_RSLT.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 32  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CONTINUED_CARE_SERVICE_C_NAME` | VARCHAR | org | The category ID for the service used to generate a list of post-discharge service providers for this patient. |
| 6 | `SEARCH_LOCATION_TYPE_C_NAME` | VARCHAR |  | The category ID for the type of location used to generate the list of service providers |
| 7 | `SEARCH_LOCATION` | VARCHAR |  | The location used to generate the list of service providers. The format will vary based on the type of location used to search. |
| 8 | `SEARCH_RADIUS` | NUMERIC |  | The radius from the location in miles searched to generate the list. |
| 9 | `USER_ID` | VARCHAR | FK→ | The unique ID associated with the user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| 10 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `GENERATION_UTC_DTTM` | DATETIME (UTC) |  | The UTC date/time the list of service providers was generated at. |
| 12 | `SEARCH_LIST_IDENT` | INTEGER |  | An ID for the list of service providers that is unique within the patient encounter it is on. This column is frequently used to link to the PAT_SVC_PROV_SEARCH_RSLT table. |
| 13 | `SEARCH_LOCATION_CITY` | VARCHAR |  | The city that is part of the location used to generate a list of service providers |
| 14 | `SEARCH_LOCATION_STATE_C_NAME` | VARCHAR | org | The state that is part of the location used to generate a list of service providers |
| 15 | `SEARCH_LOCATION_ZIP` | VARCHAR |  | The zip code that is part of the location used to generate a list of service providers |
| 16 | `SEARCH_LOCATION_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 17 | `SEARCH_LOCATION_FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 18 | `PRIMARY_SVC_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 19 | `FILTER_BY_AGE_YN` | VARCHAR |  | This item represents whether the service provider list was filtered to exclude facilities ineligible based on patient age. |
| 20 | `SENSITIVE_YN` | VARCHAR |  | This represents whether the service provider list is considered sensitive. |
| 21 | `COORDINATION_PLAN_IDENT` | VARCHAR |  | This item holds the unique ID of the Coordination Plan from which this list was generated (if generated within Services to Coordinate). This ID links service provider lists to EPT related group 97110 which stores information of Coordination Plans. |
| 22 | `FILTER_BY_AVAIL_YN` | VARCHAR |  | This item represents whether the service provider list was filtered to exclude facilities that do not have availability. |
| 23 | `HAS_PARTNERS_YN` | VARCHAR |  | This item represents whether the service provider list has any preferred partners on it. |
| 24 | `PREF_PARTNER_GROUP_C_NAME` | VARCHAR | org | The Accountable Care Organization (ACO) partner group (I EAF 34146) used to filter a patient choice list. |
| 25 | `FILTER_BY_AREA_SERVED_YN` | VARCHAR |  | This item represents whether the service provider list was filtered to exclude facilities ineligible based on area served. |
| 26 | `SEARCH_LOCATION_COUNTY_2_C_NAME` | VARCHAR | org | The county that is part of the location used to generate a list of service providers |
| 27 | `SEARCH_BY_AREA_YN` | VARCHAR |  | This item represents whether the service provider list was created using an area served search. |
| 28 | `FILTER_BY_ACCEPTED_YN` | VARCHAR |  | This item represents whether the service provider list was filtered to include facilities that accepted a service request for the patient. |
| 29 | `FILTER_BY_CONSIDERING_YN` | VARCHAR |  | This item represents whether the service provider list was filtered to include facilities that marked a service request for the patient as considering. |
| 30 | `FILTER_BY_PENDING_YN` | VARCHAR |  | This item represents whether the service provider list was filtered to include facilities that have a pending service request for the patient. |
| 31 | `FILTER_BY_DECLINED_YN` | VARCHAR |  | This item represents whether the service provider list was filtered to include facilities that declined a service request for the patient. |
| 32 | `FILTER_BY_NO_REQUEST_SENT_YN` | VARCHAR |  | This item represents whether the service provider list was filtered to include facilities that have no request status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

