# ATB_AUTH_ENTITIES

> The Auth Entities table contains information about the providers and locations associated with an authorization request. A row in this table represents a single entity, with the data columns representing specific pieces of information about the entity.

**Primary key:** `AUTH_BUNDLE_ID`, `LINE`  
**Columns:** 22  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the auth bundle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ENTITY_ID_REF` | VARCHAR |  | The unique identifier for the entity related line. Unique among all related group lines on the Auth Bundle. |
| 4 | `AUTH_ENTITY_TYPE_C_NAME` | VARCHAR |  | The Auth Entity Type category ID for this auth entity. |
| 5 | `ENTITY_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `ENTITY_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 7 | `ENTITY_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 8 | `ENTITY_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 9 | `ENTITY_HOUSE_NUM` | VARCHAR |  | The house number associated with the entity's address information. |
| 10 | `ENTITY_CITY` | VARCHAR |  | The city associated with the entity's address information. |
| 11 | `ENTITY_STATE_C_NAME` | VARCHAR | org | The State category ID for this auth entity's address information. |
| 12 | `ENTITY_ZIP` | VARCHAR |  | The ZIP code associated with the entity's address information. |
| 13 | `ENTITY_DISTRICT_C_NAME` | VARCHAR | org | The District category ID for this auth entity's address information. |
| 14 | `ENTITY_COUNTY_2_C_NAME` | VARCHAR | org | The County category ID for this auth entity's address information. |
| 15 | `ENTITY_COUNTRY_2_C_NAME` | VARCHAR | org | The Country category ID for this auth entity's address information. |
| 16 | `ENTITY_ORG_NAME` | VARCHAR |  | The entity's organization name, only used for entities that are locations (as opposed to providers). |
| 17 | `ENTITY_FIRST_NAME` | VARCHAR |  | The entity's first name, usually relevant to provider type entities. |
| 18 | `ENTITY_MIDDLE_NAME` | VARCHAR |  | The entity's middle name, usually relevant to provider type entities. |
| 19 | `ENTITY_LAST_NAME` | VARCHAR |  | The entity's last name, usually relevant to provider type entities. |
| 20 | `ENTITY_NAME_SUFFIX_C_NAME` | VARCHAR | org | The Suffix category ID for this auth entity's name information. |
| 21 | `ENTITY_AUTH_ROLE_C_NAME` | VARCHAR |  | The Auth Entity Role category ID for this auth entity's auth role. |
| 22 | `ENTITY_PRIMARY_TAXONOMY` | VARCHAR |  | The primary taxonomy code used for this entity. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

