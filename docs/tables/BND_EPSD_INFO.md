# BND_EPSD_INFO

> This table contains information about bundled episodes. A bundled episode is used to link related encounters and services that can be billed together using a pre-defined agreement with a payor or guarantor.

**Primary key:** `EPISODE_ID`  
**Columns:** 21  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the bundled episode record. |
| 2 | `COVERAGE_ID` | NUMERIC | FK→ | This column stores the unique identifier for the coverage that will be billed for the bundled episode. |
| 3 | `PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 4 | `SELF_PAY_YN` | VARCHAR |  | Indicates whether the guarantor is responsible for the bundled episode's expected payment. |
| 5 | `BPC_ID` | NUMERIC | FK→ | This column stores the unique identifier for the bundled episode terms associated with the bundled episode. The terms are used to define various reimbursement related attributes for a bundled episode. |
| 6 | `BPC_ID_BPC_NAME` | VARCHAR |  | The name of the bundled episode terms record. |
| 7 | `BPC_CSN` | NUMERIC |  | The contact serial number of the bundled episode terms associated with the bundled episode. The terms are used to define various reimbursement related attributes for a bundled episode. |
| 8 | `BILLING_START_DT` | DATETIME |  | The start date from which the services are covered in the bundled episode. |
| 9 | `BILLING_END_DT` | DATETIME |  | The end date until which the services are covered in the bundled episode. |
| 10 | `EXP_TOTAL_PMT` | NUMERIC |  | The amount of the total expected payment/target price from the responsible party of a bundled episode. |
| 11 | `EXP_HOSP_PMT` | NUMERIC |  | The amount of the total hospital expected payment from the responsible party of a bundled episode. |
| 12 | `EXP_PROF_PMT` | NUMERIC |  | The amount of the total professional expected payment from the responsible party of a bundled episode. This will only be used when a separate professional payment is expected. |
| 13 | `MAIN_EVENT_CSN` | NUMERIC |  | The contact serial number of the patient encounter that is the main encounter for this bundled episode. |
| 14 | `MAIN_EVENT_USER_ID` | VARCHAR |  | This column stores the unique identifier for the user who set the main event for this bundled episode. |
| 15 | `MAIN_EVENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 16 | `MAIN_EVENT_SET_DTTM` | DATETIME (UTC) |  | The date and time that the main event was last set for this bundled episode. |
| 17 | `CLOSE_OR_VOID_DATE` | DATETIME |  | The closed or voided date of the bundled episode. |
| 18 | `BND_EPSD_VOID_RSN_C_NAME` | VARCHAR | org | The category ID of the reason why a bundled episode is voided. |
| 19 | `LAST_LINK_UNLINK_DATE` | DATETIME |  | The most recent date when a record was either linked or unlinked from the bundled episode. This will be updated when a hospital transaction, professional transaction, or hospital billing account is linked or unlinked. |
| 20 | `LAST_ORIG_PMT_DATE` | DATETIME |  | The most recent date when a global payment or refund was posted on the anchor hospital account. |
| 21 | `LAST_BILL_LINK_UNLINK_DT` | DATETIME |  | The most recent date when a record was either linked or unlinked from the bundled episode within the date range of a non-tracking phase. This will be updated when a hospital transaction, professional transaction, or hospital billing account is linked or unlinked. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BPC_ID` | [BND_EPSD_TERMS](BND_EPSD_TERMS.md) | sole_pk | high |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

