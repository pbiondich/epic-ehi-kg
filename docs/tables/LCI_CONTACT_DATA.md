# LCI_CONTACT_DATA

> Clarity table for overtime single items in LCI.

**Primary key:** `EXTERNAL_CVG_ID`, `CONTACT_DATE_REAL`  
**Columns:** 38  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EXTERNAL_CVG_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the external coverage record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `GROUP_CODE` | VARCHAR |  | The group code of an external coverage contact. |
| 4 | `GROUP_NAME` | VARCHAR |  | The group name of an external coverage contact. |
| 5 | `PLAN_TYPE_C_NAME` | VARCHAR | org | The plan type of an external coverage contact. |
| 6 | `PLAN_NAME` | VARCHAR |  | The plan name of an external coverage contact. |
| 7 | `PAYER_NAME` | VARCHAR |  | The payer name of an external coverage contact. |
| 8 | `CVG_EFF_DATE` | DATETIME |  | The coverage effective date of an external coverage contact. |
| 9 | `CVG_TERM_DATE` | DATETIME |  | The coverage termination date of an external coverage contact. |
| 10 | `CVG_ADJ_TYPE` | INTEGER |  | The coverage adjustment type of an external coverage contact. |
| 11 | `CVG_ADJ_SEQUENCE` | INTEGER |  | The coverage adjustment sequence of an external coverage contact. |
| 12 | `CVG_STATUS_C_NAME` | VARCHAR |  | The coverage status of an external coverage contact. |
| 13 | `PROGRAM_ID` | NUMERIC | FK→ | The contract (program) ID of an external coverage contact. |
| 14 | `PROGRAM_ID_RECORD_NAME` | VARCHAR |  | The name of the program record. |
| 15 | `REGION_NAME` | VARCHAR |  | The region name of an external coverage contact. |
| 16 | `LOB_ID` | VARCHAR | FK→ | The line of business of an external coverage contact. |
| 17 | `LOB_ID_LOB_NAME` | VARCHAR |  | The name of the line of business record. |
| 18 | `CORPORATION_NAME` | VARCHAR |  | The corporation name of an external coverage contact. |
| 19 | `PAT_PRIMARY_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 20 | `ENROLLMENT_CAT_C_NAME` | VARCHAR | org | The enrollment category of an external coverage contact. |
| 21 | `REL_CODE_SET_C_NAME` | VARCHAR |  | The relationship code set of an external coverage contact. |
| 22 | `SUBSCRIBER_NAME` | VARCHAR |  | The subscriber name for an external coverage contact. |
| 23 | `SUBSCRIBER_DOB_DATE` | DATETIME |  | The subscriber date of birth for an external coverage contact. |
| 24 | `SUBSCRIBER_SEX_C_NAME` | VARCHAR | org | The subscriber sex for an external coverage contact. |
| 25 | `MEM_REL_TO_SUB_C_NAME` | VARCHAR | org | The member's relationship to the subscriber for an external coverage contact. |
| 26 | `GROUP_NUMBER` | VARCHAR |  | The group number for an external coverage contact. |
| 27 | `EXT_DEMOG_ID` | NUMERIC |  | The REQ that this LCI is attached to at this timestamp. |
| 28 | `CARRIER_ID` | VARCHAR | FK→ | Carrier (MCR) record associated with the patient's coverage. |
| 29 | `CARRIER_ID_CARRIER_NAME` | VARCHAR |  | The name of the carrier record. |
| 30 | `CARRIER_NAME` | VARCHAR |  | Name of the carrier associated with the patient's coverage. |
| 31 | `PRIM_CARE_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 32 | `REL_CODE` | VARCHAR |  | The patient's relationship to the subscriber. |
| 33 | `COMPILED_TERM_DATE` | DATETIME |  | The compiled termination date for an eligibility period. Populated during filing if there is no termination date on the eligibility period. |
| 34 | `IS_MEDICARE_ESRD_YN` | VARCHAR |  | Indicates if the member is covered by Medicare with an enrollment category of ESRD (End Stage Renal Disease). |
| 35 | `MCARE_MCAID_DUAL_STAT_C_NAME` | VARCHAR |  | The Medicaid dual status code for a member that is covered by Medicare. |
| 36 | `PROD_TYPE_C_NAME` | VARCHAR | org | The product type for an external coverage contact. |
| 37 | `PLAN_GRP_ID` | VARCHAR | FK→ | The employer group associated with the eligibility information. |
| 38 | `PLAN_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CARRIER_ID` | [CLARITY_CARRIER](CLARITY_CARRIER.md) | sole_pk | high |
| `LOB_ID` | [CLARITY_LOB](CLARITY_LOB.md) | sole_pk | high |
| `PLAN_GRP_ID` | [PLAN_GRP](PLAN_GRP.md) | sole_pk | high |
| `PROGRAM_ID` | [VALUE_BASED_PROGRAM](VALUE_BASED_PROGRAM.md) | sole_pk | high |

