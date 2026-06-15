# COVERAGE_5

> The COVERAGE_5 table contains high-level information on both managed care and indemnity coverage records in your system.

**Overflow of:** [COVERAGE](COVERAGE.md)  
**Primary key:** `CVG_ID`  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK | The unique identifier (.1 item) for the coverage record. |
| 2 | `COBA_STATUS_C_NAME` | VARCHAR |  | The Coordination of Benefits Agreement (COBA) status for E01 file generation. |
| 3 | `COBA_DELETE_EFF_DATE` | DATETIME |  | When the Coordination of Benefits Agreement (COBA) status in COBA_STATUS_C is DELETE or ADD+DELETE, this holds the effective date that is to be marked as deleted on the E01 file. |
| 4 | `PLAN_MAPPING_SKIP_OLD_CVG_ID` | NUMERIC |  | The source coverage that the plan swap was performed on to create this coverage |
| 5 | `PLAN_MAPPING_SKIP_STATUS_C_NAME` | VARCHAR |  | Stores the current status of plan mapping skip behavior |
| 6 | `PLAN_MAPPING_SKIP_DATE` | DATETIME |  | The date that the plan swap took place. |
| 7 | `PLAN_MAPPING_SKIP_USER_ID` | VARCHAR |  | The user that last updated the plan mapping skip status |
| 8 | `PLAN_MAPPING_SKIP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `MCARE_GENDER_IDENTITY_C_NAME` | VARCHAR |  | The gender identity denoted by the subscriber on their Medicare Advantage application. |
| 10 | `MCARE_SEX_ORIENTATION_C_NAME` | VARCHAR |  | The sexual orientation denoted by the subscriber on their Medicare Advantage application. |
| 11 | `MCARE_SPEC_GENDER_IDENTITY` | VARCHAR |  | The term the subscriber specified for their gender identity on their Medicare Advantage application because a value for their gender identity was not present on the application. |
| 12 | `MCARE_SPEC_SEX_ORIENTATION` | VARCHAR |  | The term the subscriber specified for their sexual orientation on their Medicare Advantage application because a value for their sexual orientation was not present on the application. |
| 13 | `MCARE_INDIV_REP_NAME` | VARCHAR |  | The name of the individual representative that helped the subscriber fill out their Medicare Advantage application. |
| 14 | `MCARE_INDIV_REP_REL_C_NAME` | VARCHAR |  | The relationship of the individual representative to the subscriber that they helped fill out the Medicare Advantage application for. |
| 15 | `MCARE_INDIV_REP_NPN` | VARCHAR |  | The National Producer Number of the individual representative that helped the subscriber fill out the Medicare Advantage application, if the individual representative is an agent or a broker. |
| 16 | `PRIMARY_COVERAGE_ID` | NUMERIC |  | The unique ID of the coverage that represents the primary coverage for this coverage. The primary coverage is logically the same coverage as this coverage and other coverages that are associated with them. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [COVERAGE](COVERAGE.md).

