# ADDR_HX

> This table extracts each patient's historical addresses.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 15  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADDR_HX_CITY` | VARCHAR |  | This item stores the city from a patient's historical address. |
| 4 | `ADDR_HX_STATE_C_NAME` | VARCHAR | org | This item stores the state from a patient's historical address. |
| 5 | `ADDR_HX_ZIP` | VARCHAR |  | This item stores the postal code from a patient's historical address. |
| 6 | `ADDR_HX_COUNTY_C_NAME` | VARCHAR | org | This item stores the county from a patient's historical address. |
| 7 | `ADDR_HX_COUNTRY_C_NAME` | VARCHAR | org | This item stores the country from a patient's historical address. |
| 8 | `ADDR_HX_HOUSE_NUM` | VARCHAR |  | This item stores the house number from a patient's historical address. |
| 9 | `ADDR_HX_DISTRICT_C_NAME` | VARCHAR | org | This item stores the district from a patient's historical address. |
| 10 | `ADDR_HX_CONTACT` | VARCHAR |  | This item stores the name of the contact person associated with a patient's historical address. |
| 11 | `ADDR_HX_PURPOSE_C_NAME` | VARCHAR | org | This item stores the purpose of a patient's historical address. |
| 12 | `ADDR_HX_START_DT` | DATETIME |  | This item stores the date on which a patient's historical address became effective. |
| 13 | `ADDR_HX_END_DT` | DATETIME |  | This item stores the date on which a patient's historical address is no longer effective. |
| 14 | `ADDR_HX_PDS_IDNT` | VARCHAR |  | This item stores the unique identifier assigned to a patient's historical address by the Personal Demographics Service. |
| 15 | `ADDR_HX_TYPE_C_NAME` | VARCHAR |  | This item stores the address type of a patient's historical address. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

