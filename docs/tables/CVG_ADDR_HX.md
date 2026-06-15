# CVG_ADDR_HX

> This table extracts each coverage's historical addresses.

**Primary key:** `CVG_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADDR_HX_CITY` | VARCHAR |  | This item is used to store the city listed in a coverage's historical address. |
| 4 | `ADDR_HX_STATE_C_NAME` | VARCHAR | org | This item is used to store the state listed in a coverage's historical address. |
| 5 | `ADDR_HX_ZIP` | VARCHAR |  | This item is used to store the ZIP code listed in a coverage's historical address. |
| 6 | `ADDR_HX_COUNTY_C_NAME` | VARCHAR | org | This item is used to store the county listed in a coverage's historical address. |
| 7 | `ADDR_HX_COUNTRY_C_NAME` | VARCHAR | org | This item is used to store the country listed in a coverage's historical address. |
| 8 | `ADDR_HX_HOUSE_NUM` | VARCHAR |  | This item is used to store the house number listed in a coverage's historical address. |
| 9 | `ADDR_HX_DISTRICT_C_NAME` | VARCHAR | org | This item is used to store the district listed in a coverage's historical address. |
| 10 | `ADDR_HX_CONTACT` | VARCHAR |  | This item is used to store the name of the contact person associated with a coverage's historical address. |
| 11 | `ADDR_HX_START_DT` | DATETIME |  | This item is used to store the date on which a coverage's historical address became effective. |
| 12 | `ADDR_HX_END_DT` | DATETIME |  | This item is used to store the date on which a coverage's historical address is no longer effective. |
| 13 | `ADDR_HX_PDS_IDNT` | VARCHAR |  | This item is used to store the unique identifier assigned to a coverage's historical address by the Personal Demographics Service. |
| 14 | `ADDR_HX_TYPE_C_NAME` | VARCHAR |  | This item is used to store the address type of a coverage's historical address. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |

