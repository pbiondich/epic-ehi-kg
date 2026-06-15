# HM_PAT_ATTEST_HISTORY

> The HM_PAT_ATTEST_HISTORY table contains information about current and past Health Maintenance patient attestations that were submitted through MyChart. This includes the data the patient submitted as well as information about who last acted on the attestation.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HM_ATTEST_PHONE_NUMBER` | VARCHAR |  | Stores the phone number of the location where a patient attested a Health Maintenance topic was completed. |
| 4 | `HM_ATTEST_ST_ADDRESS` | VARCHAR |  | Stores the street address of the location where a patient attested a Health Maintenance topic was completed. |
| 5 | `HM_ATTEST_CITY` | VARCHAR |  | Stores the city portion of the address of the location where a patient attested a Health Maintenance topic was completed. |
| 6 | `HM_ATTEST_TAX_STATE_C_NAME` | VARCHAR | org | Stores the state portion of the address of the location where a patient attested a Health Maintenance topic was completed. |
| 7 | `HM_ATTEST_ZIP` | VARCHAR |  | Stores the zip code portion of the address of the location where a patient attested a Health Maintenance topic was completed. |
| 8 | `HM_ATTEST_COUNTY_2_C_NAME` | VARCHAR | org | Stores the county portion of the address of the location where a patient attested a Health Maintenance topic was completed. |
| 9 | `HM_ATTEST_COUNTRY_2_C_NAME` | VARCHAR | org | Stores the country portion of the address of the location where a patient attested a Health Maintenance topic was completed. |
| 10 | `HM_ATTEST_HOUSE_NUMBER` | VARCHAR |  | Stores the house number portion of the address of the location where a patient attested a Health Maintenance topic was completed. |
| 11 | `HM_ATTEST_DISTRICT_C_NAME` | VARCHAR | org | Stores the district portion of the address of the location where a patient attested a Health Maintenance topic was completed. |
| 12 | `HM_ATTEST_BUILDING_NAME` | VARCHAR |  | Stores the building name portion of the address of the location where a patient attested a Health Maintenance topic was completed. |
| 13 | `HM_ATTEST_FLOOR` | VARCHAR |  | Stores the floor portion of the address of the location where a patient attested a Health Maintenance topic was completed. |
| 14 | `HM_ATTEST_UNIT` | VARCHAR |  | Stores the unit portion of the address of the location where a patient attested a Health Maintenance topic was completed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

