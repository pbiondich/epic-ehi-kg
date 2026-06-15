# HC_PLACE_OF_SRVC

> This table contains home care place of service information.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 23  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LEVEL_OF_CARE_C_NAME` | VARCHAR |  | This item stores the level of care changes for a hospice patient |
| 4 | `HOME_CARE_POS_DT` | DATETIME |  | This item tracks a starting date for the place of service of a home care patient. |
| 5 | `PLACE_OF_SERVICE_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 6 | `POS_ADDRESS` | VARCHAR |  | Street address of the home care place of service |
| 7 | `POS_CITY` | VARCHAR |  | This item tracks the city of the home care patient's place of service |
| 8 | `POS_STATE_C_NAME` | VARCHAR | org | This item tracks the state of the home care patient's place of service |
| 9 | `POS_ZIP` | VARCHAR |  | This item tracks the zip code of the home care patient's place of service |
| 10 | `POS_TYPE_C_NAME` | VARCHAR | org | This item tracks the type of location for a home care patient's place of service. |
| 11 | `POS_COMMENTS` | VARCHAR |  | This item tracks free text comments about the place of service and/or hospice level of care. |
| 12 | `POS_EDIT_USER_ID` | VARCHAR |  | This item tracks the user who last edited this line of the place of service or level of care. |
| 13 | `POS_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 14 | `POS_EDIT_DTTM` | DATETIME (UTC) |  | This item tracks the instant at which this place of service entry was last edited. |
| 15 | `HSPC_ROOM_BOARD_YN` | VARCHAR |  | This item stores whether or not room and board charges should be generated for this place of service entry. |
| 16 | `POS_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 17 | `POS_COUNTY_C_NAME` | VARCHAR | org | This item tracks the county of the home care patient's place of service |
| 18 | `POS_COUNTRY_2_C_NAME` | VARCHAR | org | This column tracks the country category value for a home care patient's place of service. |
| 19 | `POS_HOUSE_NUMBER` | VARCHAR |  | This column tracks the house number for a home care patient's place of service. |
| 20 | `POS_DISTRICT_C_NAME` | VARCHAR | org | This column tracks the district category value for a home care patient's place of service. |
| 21 | `LATITUDE` | VARCHAR |  | The geocoded latitude of the place of service address in decimal degrees with up to 6 decimals of accuracy. |
| 22 | `LONGITUDE` | VARCHAR |  | The geocoded longitude for the place of service address with 6 decimals of precision. |
| 23 | `GEO_RATING` | VARCHAR |  | The GEO_RATING rates the accuracy of latitude and longitude for a given place of service address. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

