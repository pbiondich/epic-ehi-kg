# PR_EST_PX_BEN_ADDL_INFO

> Contains additional benefit related information for each procedure in a price estimate.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 28  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the patient estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADDL_LINE_NUM` | INTEGER |  | The line number of the additional information charge line group. |
| 4 | `FILE_ORD_NUM` | INTEGER |  | The coverage level associated with the corresponding coverage (I PES 168). |
| 5 | `SERVICE_TYPE_ID` | VARCHAR | FK→ | The service type associated with the benefits on an estimate line. |
| 6 | `SERVICE_TYPE_ID_SERVICE_TYPE_NAME` | VARCHAR |  | The name of this benefit service type. |
| 7 | `PAYER_BEN_CAT` | VARCHAR |  | The benefit category identifier supplied by the payer. This is used instead of a service type in estimates adjudicated by the payer. It should only be set on an estimate reference benefits. |
| 8 | `DEDUCTIBLE_AMT` | NUMERIC |  | This is the deductible amount of an estimate line. |
| 9 | `COPAY_AMT` | NUMERIC |  | This is the copay amount of an estimate line. |
| 10 | `COINS_AMT` | NUMERIC |  | This is the coinsurance amount of an estimate line. |
| 11 | `SELFPAY_EXCESS_AMT` | NUMERIC |  | This is the additional self-pay amount as a result of insurance limits. |
| 12 | `MOOP_AMT` | NUMERIC |  | This is the maximum out-of-pocket amount for an estimate line. |
| 13 | `ANNUAL_LIMIT` | NUMERIC |  | This is the annual insurance limit amount of an estimate line. |
| 14 | `LIFETIME_LIMIT` | NUMERIC |  | This is the lifetime insurance limit amount of an estimate line. |
| 15 | `ROLLOVER_AMT` | NUMERIC |  | This is the rollover period amount of an estimate line. |
| 16 | `NET_LEVEL_C_NAME` | VARCHAR | org | This is the network level used to calculate benefits of an estimate line. |
| 17 | `VISIT_MOOP_AMT` | NUMERIC |  | This is the visit maximum out-of-pocket amount for an estimate line. |
| 18 | `VISIT_LIMIT` | NUMERIC |  | This is the amount of an estimate line applied to a visit insurance limit. |
| 19 | `PROV_TOTAL` | NUMERIC |  | The total the Provider is estimated pay for an estimate line. |
| 20 | `NONCVRD_AMT` | NUMERIC |  | Amount not covered by a member's benefits for an estimate line. |
| 21 | `AMT_EXCEEDED` | NUMERIC |  | The amount that exceeded the benefit amount from the estimate line. |
| 22 | `BEN_BKT_ID` | NUMERIC |  | The ID of the bucket that the estimate line contributes to. |
| 23 | `BEN_BKT_ID_BUCKET_NAME` | VARCHAR |  | The name of the bucket. |
| 24 | `BEN_BKT_LIMIT` | NUMERIC |  | The maximum amount the bucket can hold. |
| 25 | `BEN_BKT_ADDL_AMT` | NUMERIC |  | Additional amount added to the bucket from the estimate line. |
| 26 | `BEN_BKT_REMAIN` | NUMERIC |  | Amount left in the bucket after adding the additional amount from the estimate line. |
| 27 | `LTC_MONTHLY_AMT` | NUMERIC |  | This is the Monthly Patient Pay Amount of an estimate line |
| 28 | `COINS_PERCENT` | NUMERIC |  | This is the coinsurance percentage for this procedure line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SERVICE_TYPE_ID` | [BENEFIT_SVC_TYPE](BENEFIT_SVC_TYPE.md) | sole_pk | high |

