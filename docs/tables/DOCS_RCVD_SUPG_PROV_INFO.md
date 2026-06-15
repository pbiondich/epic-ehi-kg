# DOCS_RCVD_SUPG_PROV_INFO

> This table contains information about the supervising provider of the e-prescription.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 20  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `SUPG_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `SUPG_PROV_NAME` | VARCHAR |  | Name for the supervising provider |
| 6 | `SUPG_PROV_WORK_PH` | VARCHAR |  | Work phone number for the supervising provider |
| 7 | `SUPG_PROV_FAX` | VARCHAR |  | Fax number for the supervising provider |
| 8 | `SUPG_PROV_EMAIL` | VARCHAR |  | E-mail address for the supervising provider |
| 9 | `SUPG_PROV_ADD_STREE` | VARCHAR |  | Street address for the supervising provider |
| 10 | `SUPG_PROV_ADDR_CITY` | VARCHAR |  | City for the supervising provider work address |
| 11 | `SUPG_PROV_ADDR_ST_C_NAME` | VARCHAR | org | The specialties ID for the supervising provider work address |
| 12 | `SUPG_PROV_ADDR_ZIP` | VARCHAR |  | Zip code for the supervising provider work address |
| 13 | `SUPG_PROV_SPEC_NAME` | VARCHAR |  | Free text list of supervising provider specialty names |
| 14 | `SUPG_PROV_SPEC_C_NAME` | VARCHAR | org | The state category ID for the supervising provider. |
| 15 | `SUPG_PROV_DEA_NUM` | VARCHAR |  | DEA number of the supervising provider |
| 16 | `SUPG_PROV_ST_LIC_NU` | VARCHAR |  | State license number of the supervising provider |
| 17 | `SUPG_PROV_NPI` | VARCHAR |  | National Provider Identifier (NPI) number of the supervising provider |
| 18 | `SUPG_PROV_CLINIC_NM` | VARCHAR |  | Clinic name where the supervising provider practices |
| 19 | `ERX_IS_REFILL_FOLLOWUP_YN` | VARCHAR |  | Identifies whether the provider on this line of the group is a refill follow-up provider. |
| 20 | `SUPG_PROV_NAME_SUFFIX` | VARCHAR |  | Stores suffixes for the supervising provider's name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

