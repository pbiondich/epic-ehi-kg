# AUTH_REQUEST_HX_ENT_INFO

> This table contains information about entity information related to the Authorization Request.

**Primary key:** `AUTH_REQUEST_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 20  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_REQUEST_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the authorization request record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `ENT_TYPE_C_NAME` | VARCHAR |  | The type of the entity in this prior authorization. |
| 5 | `ENT_ROLE_C_NAME` | VARCHAR |  | The role of the entity in this prior authorization. |
| 6 | `ENT_FAC_NAME` | VARCHAR |  | The name of the facility in this prior authorization. |
| 7 | `ENT_PROV_FIRST_NAME` | VARCHAR |  | The first name of the provider in this prior authorization. |
| 8 | `ENT_PROV_MID_NAME` | VARCHAR |  | The middle name of the provider in this prior authorization. |
| 9 | `ENT_PROV_LAST_NAME` | VARCHAR |  | The last name of the provider in this prior authorization. |
| 10 | `ENT_TAX_CODE` | VARCHAR |  | Taxonomy codes of a provider/location. |
| 11 | `ENT_NPI` | VARCHAR |  | NPI for the entity. |
| 12 | `ENT_TIN` | VARCHAR |  | Tax ID for the entity. |
| 13 | `ENT_PHONE` | VARCHAR |  | Phone number for the entity. |
| 14 | `ENT_FAX` | VARCHAR |  | Fax number for the entity. |
| 15 | `ENT_EMAIL` | VARCHAR |  | The contact email for the entity. |
| 16 | `ENT_ADDR_LINE_1` | VARCHAR |  | The first line of a street address of the entity. |
| 17 | `ENT_ADDR_LINE_2` | VARCHAR |  | The second line of a street address of the entity. |
| 18 | `ENT_ADDR_CITY` | VARCHAR |  | City for the address of the entity. |
| 19 | `ENT_TAX_STATE_C_NAME` | VARCHAR | org | State for the address of the entity. |
| 20 | `ENT_ADDR_ZIP` | VARCHAR |  | ZIP code of the address of the entity. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_REQUEST_ID` | [AUTH_REQUEST](AUTH_REQUEST.md) | sole_pk | high |

