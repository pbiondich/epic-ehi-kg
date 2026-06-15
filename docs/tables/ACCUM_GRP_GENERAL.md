# ACCUM_GRP_GENERAL

> This table contains general information about accumulation group (ACG) records.

**Primary key:** `ACCUM_GRP_ID`  
**Columns:** 36  
**Org-specific columns:** 3  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCUM_GRP_ID` | NUMERIC | PK | The unique identifier (.1 item) for the accumulation group record. |
| 2 | `BUCKET_ID` | NUMERIC | shared | The ID of the benefit bucket being accumulated to. |
| 3 | `BUCKET_ID_BUCKET_NAME` | VARCHAR |  | The name of the bucket. |
| 4 | `RLL_START_DATE` | DATETIME |  | The start date of the roll period accumulations are being made in. |
| 5 | `RECENT_ACC_ID` | NUMERIC |  | The ID of the most recent accumulation made to the accumulation group. |
| 6 | `RECENT_ACC_LN` | INTEGER |  | The line in related group 60 from the accumulation corresponding to the most recent accumulation instance. |
| 7 | `PLAN_GRP_ID` | VARCHAR | FK→ | The ID of the associated employer group. |
| 8 | `PLAN_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |
| 9 | `PAT_ID` | VARCHAR | FK→ | The ID of the associated member. |
| 10 | `EX_ACC_ID` | NUMERIC |  | The accumulation which pushed the running total over the limit |
| 11 | `EX_ACC_LN` | INTEGER |  | The line in Related group 60 for the ACC that pushed the running total over the limit corresponding to the instance which exceeded the limit |
| 12 | `RLL_END_DATE` | DATETIME |  | The end date of the roll period accumulations are being made in. |
| 13 | `BUCKET_LEVEL` | INTEGER |  | The bucket level associated with this ACG, if applicable. |
| 14 | `BUCKET_PAYMENT_MECHANISM_C_NAME` | VARCHAR |  | The payment mechanism of the associated bundle bucket at this level, which determines how associated services are priced. |
| 15 | `BUCKET_LIMIT_AMOUNT` | NUMERIC |  | The amount limit associated with this bucket level. |
| 16 | `FUN_TYP_C_NAME` | VARCHAR |  | The functional type that specifies which workflows can interact with this accumulation group. |
| 17 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc...) |
| 18 | `ASSOC_SPECIALTY_C_NAME` | VARCHAR | org | The claim specialty associated with the accumulation group |
| 19 | `BEN_LIM_ACCUM_GRP_ID` | NUMERIC |  | The benefit limit ACG that the visit originated with. Due to carryover, the visit ACG may be on other benefits ACG's besides this, and may even have originally accumulated to those; this just tracks where the first line was. |
| 20 | `BEN_LIM_ACCUM_GRP_ST_TOT` | NUMERIC |  | The total of the benefit limit accumulation group when this visit was created. |
| 21 | `ACCUM_GRP_COVERAGE_ID` | NUMERIC |  | Coverage ID associated with the accumulation group. |
| 22 | `CURRENT_RUNNING_TOTAL` | NUMERIC |  | The total accumulations that have been made. This item links to the most recent accumulation line's (I ACG 50/51) running total (I ACC 94). |
| 23 | `ACCUM_BEN_FUNCTION_C_NAME` | VARCHAR | org | The function of the benefits engine evaluator that generated the accumulation. The system uses this item to categorize the purposes of the accumulation group. |
| 24 | `ACCUM_BEN_EVAL_ORDER` | INTEGER |  | The function order of the benefits engine evaluator that generated the accumulation. The system uses this item to categorize the purposes of the accumulation group. |
| 25 | `COUNTED_UNIT_TYPE_C_NAME` | VARCHAR |  | The type of entity counted by this accumulation group. |
| 26 | `ACCUM_GRP_NETWORK_LEVEL_C_NAME` | VARCHAR | org | The network level associated with the accumulation group. |
| 27 | `ACCUM_GRP_BEN_VAR_ID` | NUMERIC |  | The grouper keyword associated with the accumulation group. |
| 28 | `ACCUM_GRP_BEN_VAR_ID_BEN_VAR_NAME` | VARCHAR |  | The name of the benefit variable. |
| 29 | `ACCUM_GRP_PROC_CD` | VARCHAR |  | The procedure code associated with the accumulation group. |
| 30 | `ACCUM_GRP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 31 | `ACCUM_GRP_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 32 | `ACCUM_GRP_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 33 | `ACCUM_GRP_PAYMENT_MECH_ID` | NUMERIC |  | The payment mechanism associated with the accumulation group. |
| 34 | `ACCUM_GRP_PAYMENT_MECH_ID_PAYMENT_MECH_NAME` | VARCHAR |  | The name of the payment mechanism record. |
| 35 | `ACCUM_GRP_CLAIM_ID` | NUMERIC |  | The claim associated with the accumulation group. This is only populated if the limit is set to apply per claim. |
| 36 | `ACCUM_SRC_C_NAME` | VARCHAR |  | The Source Type of the accumulation group. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `PLAN_GRP_ID` | [PLAN_GRP](PLAN_GRP.md) | sole_pk | high |

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [ACCUM_GRP_PAT_PMT_RMT](ACCUM_GRP_PAT_PMT_RMT.md) | `ACCUM_GRP_ID` | high |
| [ACCUM_GRP_SVC_DATE](ACCUM_GRP_SVC_DATE.md) | `ACCUM_GRP_ID` | high |

