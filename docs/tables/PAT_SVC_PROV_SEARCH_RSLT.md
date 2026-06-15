# PAT_SVC_PROV_SEARCH_RSLT

> This table stores service providers on a list of post-discharge service providers that was given to a patient so that they can indicate their preference. The criteria used to generate each list and the user who generated it are in PAT_SVC_PROV_SEARCH_LIST.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `SEARCH_LIST_IDENT` | INTEGER |  | An ID for the list of service providers that the result is a part of. This column is frequently used to link to the PAT_SVC_PROV_SEARCH_LIST table. |
| 6 | `FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 7 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 9 | `DISTANCE` | NUMERIC |  | The distance in miles of the service provider in the list from the search location. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

