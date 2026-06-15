# ATB_AUTH_CONTACTS

> This table stores contacts relevant to the authorization.

**Primary key:** `AUTH_BUNDLE_ID`, `LINE`  
**Columns:** 21  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the auth bundle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONTACT_ID_REF` | VARCHAR |  | The reference ID for this particular authorization contact line. |
| 4 | `AUTH_CONTACT_TYPE_C_NAME` | VARCHAR |  | The broad categorization for this particular contact, for example differentiating between an administrative point of contact or a payer delegate. |
| 5 | `CONTACT_HOUSE_NUM` | VARCHAR |  | The house number associated with the contact's address information. |
| 6 | `CONTACT_CITY` | VARCHAR |  | The city associated with the contact's address information. |
| 7 | `CONTACT_TAX_STATE_C_NAME` | VARCHAR | org | The state associated with the contact's address information. |
| 8 | `CONTACT_ZIP` | VARCHAR |  | The ZIP code associated with the contact's address information. |
| 9 | `CONTACT_DISTRICT_C_NAME` | VARCHAR | org | The district associated with the contact's address information. |
| 10 | `CONTACT_COUNTY_2_C_NAME` | VARCHAR | org | The county associated with the contact's address information. |
| 11 | `CONTACT_COUNTRY_2_C_NAME` | VARCHAR | org | The country associated with the contact's address information. |
| 12 | `CONTACT_ORG_NAME` | VARCHAR |  | The contact's organization name. |
| 13 | `CONTACT_FIRST_NAME` | VARCHAR |  | The contact's first name. |
| 14 | `CONTACT_MIDDLE_NAME` | VARCHAR |  | The contact's middle name. |
| 15 | `CONTACT_LAST_NAME` | VARCHAR |  | The contact's last name. |
| 16 | `CONTACT_SUFFIX_C_NAME` | VARCHAR | org | The contact's name suffix. |
| 17 | `CONTACT_PHONE_NUM` | VARCHAR |  | The contact's phone number. |
| 18 | `CONTACT_FAX_NUMBER` | VARCHAR |  | The contact's fax number. |
| 19 | `CONTACT_EMAIL` | VARCHAR |  | The contact's email address. |
| 20 | `CONTACT_URL` | VARCHAR |  | The contact's URL. |
| 21 | `CONTACT_NAME_FOR_LN` | VARCHAR |  | The contact name of the person or place that should be contacted if contacting the contact referenced in the rest of this line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

