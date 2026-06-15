# COVERAGE_LOC_PCP

> This table contains coverage level primary location and PCP information.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 26  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MEMBER_ID` | VARCHAR |  | The ID of the patient associated with the coverage level primary location and PCP. |
| 4 | `PCP_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `PCP_TYPE_C_NAME` | VARCHAR | org | The PCP type for the coverage level PCP. |
| 6 | `LOCATION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 7 | `EFF_DATE` | DATETIME |  | The effective date for the coverage level primary location and PCP. |
| 8 | `TERM_DATE` | DATETIME |  | The termination date for the coverage level primary location and PCP. |
| 9 | `CHANGE_I_DTTM` | DATETIME (Local) |  | The date and time the coverage level primary location and PCP were entered or changed. |
| 10 | `CHANGE_USER_ID` | VARCHAR |  | The user that entered or changed the coverage level primary location and PCP. |
| 11 | `CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `PCP_CHANGE_RSN_C_NAME` | VARCHAR | org | The reason for changing the coverage level PCP. |
| 13 | `CHANGE_COMMENT` | VARCHAR |  | The comment entered for the coverage level primary location and PCP. |
| 14 | `DELETED_FLAG_YN` | VARCHAR |  | Indicates whether this line of coverage level primary location and PCP information has been marked as deleted. |
| 15 | `CHANGE_REQ_BY_C_NAME` | VARCHAR | org | The entity that requested a change to coverage level primary location and PCP. |
| 16 | `CVG_PCP_NETWORK_ID` | VARCHAR |  | The selected network for the member. When Member Network Selection (HDF 18885) is on this item stores the selected network for the member. This network along with the networks the member matches to based on member matching criteria in the network record will make up the network records for the member. |
| 17 | `CVG_PCP_NETWORK_ID_NETWORK_NAME` | VARCHAR |  | The name of the network. |
| 18 | `REGION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 19 | `MEDICAL_GROUP_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 20 | `PCP_ADDRESS_IDENT` | VARCHAR |  | COVERAGE PCP & LOCATION - PCP ADDRESS ID |
| 21 | `CVG_PCP_ADD_INST_LOCAL_DTTM` | DATETIME (Local) |  | The instant when the PCP and primary location are added. |
| 22 | `CVG_PCP_ADD_USER_ID` | VARCHAR |  | The user who adds the PCP and primary location. |
| 23 | `CVG_PCP_ADD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 24 | `CVG_PCP_PCP_RAW_IDENT` | VARCHAR |  | The raw PCP ID received from source when not matched to a record. |
| 25 | `CVG_PCP_PCP_RAW_NAME` | VARCHAR |  | The raw PCP name received from source when not matched to a record. |
| 26 | `CVG_PCP_LOC_RAW_IDENT` | VARCHAR |  | The raw location ID received from source when not matched to a record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

