# DOCS_RCVD_PROV_INFO

> This table contains the external provider information.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 27  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `PROV_IDENT` | VARCHAR |  | Identifier to link provider with other related groups |
| 5 | `PROV_WORK_PH` | VARCHAR |  | Work phone number for the provider |
| 6 | `PROV_FAX` | VARCHAR |  | Fax number for the provider |
| 7 | `PROV_EMAIL` | VARCHAR |  | E-mail address for the event provider |
| 8 | `PROV_ADD_STREET` | VARCHAR |  | Street address for the provider |
| 9 | `PROV_ADDR_CITY` | VARCHAR |  | City for the provider work address |
| 10 | `PROV_ADDR_STATE_C_NAME` | VARCHAR | org | State for the provider work address |
| 11 | `PROV_ADDR_ZIP` | VARCHAR |  | Zip code for the provider work address |
| 12 | `PROV_SPEC_NAME` | VARCHAR |  | Free text list of provider specialty names |
| 13 | `PROV_SPEC_C_NAME` | VARCHAR | org | List of specialties for the provider |
| 14 | `PROV_DEA_NUM` | VARCHAR |  | DEA number of the provider |
| 15 | `PROV_ST_LIC_NUM` | VARCHAR |  | State license number of the provider |
| 16 | `PROV_NPI` | VARCHAR |  | National Provider Identifier (NPI) number of the provider |
| 17 | `PROV_EXT_ID` | VARCHAR |  | External vendor identifier of the provider |
| 18 | `PROV_CLINIC_NAME` | VARCHAR |  | Clinic name where the provider practices |
| 19 | `PRESC_AGENT_NAME` | VARCHAR |  | The name of the prescriber agent who enters the prescription on behalf of the provider. |
| 20 | `PROV_SER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 21 | `PROV_CRED` | VARCHAR |  | Contains external provider credentials. |
| 22 | `PROV_ADDR_RELATED_YN` | VARCHAR |  | If this item is set to 1, then the address information in the provider related group (DXR 9000) is related. This includes items for Address - Street, City, State, Zip Code as well as Phone, Fax, Email. This means that for one line in the provider related group (DXR 9000) it can be safely assumed that the Address, Phone, Fax, and Email are all related and can be grouped and displayed together. |
| 23 | `PROV_TYPE_NAME` | VARCHAR |  | The name of the external provider's provider type. |
| 24 | `PROV_TYPE_C_NAME` | VARCHAR | org | The internal category ID of the external provider's type. |
| 25 | `PROV_PREFIX` | VARCHAR |  | Prefix of Provider's Name |
| 26 | `PROV_SUFFIX` | VARCHAR |  | Suffix of Provider's Name |
| 27 | `PROV_NADEA_NUM` | VARCHAR |  | This column contains the narcotic addiction DEA number of the provider on this line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

