# PAT_PREF_SERVICE_PROV

> This table includes information about the service providers that are marked as patient preferred in Clinical Case Management's Continued Care and Services Coordination (CCSC) tool.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `PROV_ADDR_ID` | VARCHAR |  | The address ID of the service provider the patient has indicated they prefer for an encounter for the coordination type specified (in I EPT 97204). This item is populated for provider type (SER) service providers. |
| 7 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 8 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 9 | `DP_COORD_TYPE_C_NAME` | VARCHAR | org | Coordination type of the service provider referenced in Pat Preferred Service Provider - SER ID (I EPT 97200), Pat Preferred Service Provider - EAF ID (I EPT 97202), or Pat Preferred Service Provider - EAF ID (I EPT 97203) that patient has indicated they prefer for an encounter. |
| 10 | `PAT_PREF_SVC_LN_ID` | NUMERIC |  | Service line which the patient has indicated they prefer for a service provider. |
| 11 | `PAT_PREF_SVC_LN_ID_SVC_LN_NAME` | VARCHAR |  | The name (.2 item) of the service line record. |
| 12 | `PAT_PREF_PARTNER_TIER_C_NAME` | VARCHAR | org | The facility preferred partner type that this service provider is a part of at the time of choosing it as a patient preferred service provider. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

