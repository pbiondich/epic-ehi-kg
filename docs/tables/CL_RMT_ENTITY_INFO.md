# CL_RMT_ENTITY_INFO

> This table contains the payor and payee information from the remittance file.

**Primary key:** `IMAGE_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | This is the ID for the remittance image record. |
| 2 | `ENTITY_ID_CD_C_NAME` | VARCHAR |  | Code identifying an organizational entity, a physical location, property or an individual. |
| 3 | `ENTITY_NAME` | VARCHAR |  | Free-form name |
| 4 | `ENTITY_ID_QUAL_C_NAME` | VARCHAR |  | Code designating the system/method of code structure used for Identification Code |
| 5 | `ENTITY_IDENTIFIER` | VARCHAR |  | Code identifying a party or other code |
| 6 | `ENTITY_ADDR` | VARCHAR |  | Entity's Address information |
| 7 | `ENTITY_CITY` | VARCHAR |  | Entity's city information |
| 8 | `ENTITY_STATE` | VARCHAR |  | Entity's Standard State/Province as defined by appropriate government agency |
| 9 | `ENTITY_ZIPCODE` | VARCHAR |  | Entity's ZIP code defining international postal zone code excluding punctuation and blanks (ZIP code for United States) |
| 10 | `LINE` | INTEGER | PK | The line number in the results of a query. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

