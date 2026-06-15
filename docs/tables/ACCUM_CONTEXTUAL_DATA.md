# ACCUM_CONTEXTUAL_DATA

> This table contains contextual data about a claim and service when an accumulation occurred.

**Primary key:** `ACCUMULATION_ID`  
**Columns:** 38  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCUMULATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the accumulation record. |
| 2 | `GROUPING_BEN_VAR_ID` | NUMERIC |  | Stores the benefit grouping matched to during this accumulation event. |
| 3 | `GROUPING_BEN_VAR_ID_BEN_VAR_NAME` | VARCHAR |  | The name of the benefit variable. |
| 4 | `SERVICE_BEN_VAR_ID` | NUMERIC |  | Stores the benefit service matched to during this accumulation event. |
| 5 | `SERVICE_BEN_VAR_ID_BEN_VAR_NAME` | VARCHAR |  | The name of the benefit variable. |
| 6 | `AUTH_PRES_YN` | VARCHAR |  | Stores whether an authorization was present during this accumulation event. |
| 7 | `NET_LEVEL_PROV_C_NAME` | VARCHAR | org | Stores the network level matched to during this accumulation event. |
| 8 | `EAP_CODE_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 9 | `PX_QUANTITY_CNT` | NUMERIC |  | Stores the procedure quantity for the service matched to during this accumulation event. |
| 10 | `PX_NUM_MINUTES_CNT` | INTEGER |  | Stores the procedure number of minutes for the service matched to during this accumulation event. |
| 11 | `PX_NUM_DAYS_CNT` | INTEGER |  | Stores the procedure number of days for the service matched to during this accumulation event. |
| 12 | `SERVICE_START_DATE` | DATETIME |  | Stores the service start date for the service matched to during this accumulation event. |
| 13 | `SERVICE_END_DATE` | DATETIME |  | Stores the service end date for the service matched to during this accumulation event. |
| 14 | `POS_TYPE_C_NAME` | VARCHAR | org | Stores the place of service type for the service matched to during this accumulation event. |
| 15 | `REV_CODE_ID` | NUMERIC |  | Stores the revenue code for the service matched to during this accumulation event. |
| 16 | `REV_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 17 | `CNTRCT_AMOUNT_NUM` | NUMERIC |  | Stores the contractual amount calculated for the service matched to during this accumulation event. |
| 18 | `RNDR_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 19 | `ASSOC_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 20 | `DISCH_STATUS_C_NAME` | VARCHAR | org | Stores the discharge status for the claim during this accumulation event. |
| 21 | `ATT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 22 | `ASSOC_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 23 | `ADJ_METHOD_C_NAME` | VARCHAR | org | Stores the adjudication method for the claim during this accumulation event. |
| 24 | `ASSOC_COVERAGE_ID` | NUMERIC |  | Stores the coverage for the claim during this accumulation event. |
| 25 | `CLM_SPEC_C_NAME` | VARCHAR | org | Stores the specialty for the claim during this accumulation event. |
| 26 | `CLM_FORMAT_C_NAME` | VARCHAR |  | Stores the format for the claim during this accumulation event. |
| 27 | `TYPE_OF_BILL` | VARCHAR |  | Stores the type of bill for the claim during this accumulation event. |
| 28 | `ADMISSION_DATE` | DATETIME |  | Stores the admission date for the claim during this accumulation event. |
| 29 | `DISCHARGE_DATE` | DATETIME |  | Stores the discharge date for the claim during this accumulation event. |
| 30 | `ADM_NUM_DAYS_CNT` | INTEGER |  | Stores the length of stay (days) for the claim during this accumulation event. |
| 31 | `ACCUM_DATA_SOURCE_C_NAME` | VARCHAR |  | Stores the data source type for this accumulation event. |
| 32 | `TARGET_BEN_FUNCTION_C_NAME` | VARCHAR | org | Stores the target limit type that the accumulation can apply to. Used to determine which accumulation groups the accumulation can apply to. |
| 33 | `ACCUMULATE_BY_C_NAME` | VARCHAR |  | Stores the what accumulation types this accumulation can apply to (I BEB 204 value). Used to determine which accumulation groups the accumulation can apply to. |
| 34 | `MOOP_DED_BEN_VAR_ID` | NUMERIC |  | Stores the MOOP/Deductible type (CMW ID) that the accumulation can apply to. Used to determine which accumulation groups the accumulation can apply to. |
| 35 | `MOOP_DED_BEN_VAR_ID_BEN_VAR_NAME` | VARCHAR |  | The name of the benefit variable. |
| 36 | `DRG_ID` | VARCHAR | FK→ | Stores the DRG code for the service matched to during this accumulation event. |
| 37 | `DRG_ID_DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |
| 38 | `REF_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DRG_ID` | [CLARITY_DRG](CLARITY_DRG.md) | sole_pk | high |

