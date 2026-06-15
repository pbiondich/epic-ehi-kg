# PAT_ADDR_CHNG_HX

> This table keeps track of changes in the patient's address.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 19  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | Patient ID for whom address is changed. |
| 2 | `LINE` | INTEGER | PK | Line count in the address change history. |
| 3 | `ADDR_HX_LINE1` | VARCHAR |  | First line of patient's home address, current between dates recorded in columns EFF_START_DATE and EFF_END_DATE. |
| 4 | `ADDR_HX_LINE2` | VARCHAR |  | Second line of patient's home address, current between dates recorded in columns EFF_START_DATE and EFF_END_DATE. |
| 5 | `ADDR_HX_LN_EXTRA` | VARCHAR |  | Additional line of patient's home address, current between dates recorded in columns EFF_START_DATE and EFF_END_DATE. |
| 6 | `CITY_HX` | VARCHAR |  | Patient's home city, current between dates recorded in columns EFF_START_DATE and EFF_END_DATE. |
| 7 | `COUNTY_HX_C_NAME` | VARCHAR | org | Patient's home county, current between dates recorded in columns EFF_START_DATE and EFF_END_DATE. |
| 8 | `ZIP_HX` | VARCHAR |  | Patient's home ZIP, current between dates recorded in columns EFF_START_DATE and EFF_END_DATE. |
| 9 | `ADDR_CHNG_SOURCE_C_NAME` | VARCHAR | org | Source of address changes. |
| 10 | `EFF_START_DATE` | DATETIME |  | Effective start date of changed address (date when address was changed). |
| 11 | `EFF_END_DATE` | DATETIME |  | Effective end date of changed address (date of the next address change or NULL if this is the last address change). |
| 12 | `PREV_HOUSE_NUM` | VARCHAR |  | Audit trail item used to store the previous house number when a new house number is entered or if the current primary address is edited. |
| 13 | `PREV_DISTRICT_C_NAME` | VARCHAR | org | Audit trail item used to store the previous district when a new district is entered or if the current primary address is edited. |
| 14 | `SIGNIFICANT_CHANGE_YN` | VARCHAR |  | Audit trail item used to store whether the address change should be considered significant when a new address is entered or if the current primary address is edited. |
| 15 | `ADDR_HX_VALID_YN` | VARCHAR |  | This columns specifies if the historical address stored on the patient record is invalid or incorrect. A blank value means historical address is a valid older address. Use this item to indicate a patient's address was captured due to error, for example, in the case of a patient overlay. |
| 16 | `PREV_FLOOR` | VARCHAR |  | Audit trail item used to store the previous floor number when a new floor number is entered or if the current primary address is edited. |
| 17 | `PREV_UNIT` | VARCHAR |  | Audit trail item used to store the previous unit number when a new unit number is entered or if the current primary address is edited. |
| 18 | `PREV_BLDG_NAM` | VARCHAR |  | Audit trail item used to store the previous building name when a new building is entered or if the current primary address is edited. |
| 19 | `COUNTRY_C_NAME` | VARCHAR | org | Audit trail item used to store the previous country when a new country is entered or if the current primary address is edited. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

