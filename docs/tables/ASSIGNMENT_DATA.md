# ASSIGNMENT_DATA

> This table holds the patients and roster identifiers for whom specific roster assignment data was loaded.

**Primary key:** `ASGN_DATA_ID`  
**Columns:** 21  
**Org-specific columns:** 1  
**Joined by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ASGN_DATA_ID` | NUMERIC | PK | The unique identifier (.1 item) for the assignment data record. |
| 2 | `RECORD_STATUS_2_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc...) |
| 3 | `ROSTER_IDENTIFIER_C_NAME` | VARCHAR | org | The roster population that this record contains tracking data for. |
| 4 | `PAT_ID` | VARCHAR | FK→ | The patient for whom this record contains roster tracking data. |
| 5 | `ASSIGNMENT_EFF_DATE` | DATETIME |  | The start date of the roster assignment period. |
| 6 | `ASSIGNMENT_TERM_DATE` | DATETIME |  | The end date of the roster assignment period. |
| 7 | `ATTRIBUTED_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `LAST_MODIFIED_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The instant that this roster assignment period was last loaded or backed out. |
| 9 | `EXTERNAL_DEMOG_ID` | NUMERIC |  | The unique ID of the External Demographic Set that this assignment is loaded to. |
| 10 | `EXTERNAL_IDENT_BUNDLE_ID` | NUMERIC |  | The unique ID of the External System Identifier Bundle that this assignment is loaded to. |
| 11 | `SOURCE_ORG_ID` | NUMERIC |  | The source organization for an assignment record. |
| 12 | `SOURCE_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 13 | `BLK_DTA_MESSAGE_ID` | NUMERIC |  | The AMS record that most recently created or updated this assignment record. |
| 14 | `SOURCE_ENTITY_KEY_TYPE` | VARCHAR |  | An identifier for the external system's record key type, or ID assignment system. |
| 15 | `SOURCE_ENTITY_KEY` | VARCHAR |  | The key, or unique identifier, for the record provided by the source system. |
| 16 | `SOURCE_GEN_DTTM_ASN_UTC_DTTM` | DATETIME (UTC) |  | The timestamp of the source record from the external system. |
| 17 | `VOLUNTARY_ALIGN_YN` | VARCHAR |  | Whether the beneficiary is voluntarily aligned. |
| 18 | `VOLUNTARY_ALIGN_TIN` | VARCHAR |  | The TIN of the beneficiary's designated clinician when voluntarily aligned. |
| 19 | `VOLUNTARY_ALIGN_NPI` | VARCHAR |  | The NPI of the beneficiary's designated clinician when voluntarily aligned. |
| 20 | `CLAIMS_ALIGN_YN` | VARCHAR |  | Whether the beneficiary is aligned through claims based assignment. |
| 21 | `CLAIMS_ALIGN_STEP_C_NAME` | NUMERIC |  | Indicates if the beneficiary was assigned to the ACO through Step 1, Step 2, or Step 3 of the claims-based assignment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (6)

| From | Column | Confidence |
|------|--------|------------|
| [ADDL_ASSIGNMENT_DATA](ADDL_ASSIGNMENT_DATA.md) | `ASGN_DATA_ID` | high |
| [ASSIGNMENT_DATA_LOADS](ASSIGNMENT_DATA_LOADS.md) | `ASGN_DATA_ID` | high |
| [ASSIGNMENT_DATA_MSG_HX](ASSIGNMENT_DATA_MSG_HX.md) | `ASGN_DATA_ID` | high |
| [COMPILED_ASSIGNMENT_DATA](COMPILED_ASSIGNMENT_DATA.md) | `ASGN_DATA_ID` | high |
| [COMPILED_ATTRIBUTION_DATA](COMPILED_ATTRIBUTION_DATA.md) | `ASGN_DATA_ID` | high |
| [HX_EXTERNAL_DEMOG_SETS](HX_EXTERNAL_DEMOG_SETS.md) | `ASGN_DATA_ID` | high |

