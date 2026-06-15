# BND_EPSD_HX

> This table contains the history of various changes made to bundled episodes.

**Primary key:** `EPISODE_ID`, `LINE`  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the bundled episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_UPDATE_DTTM` | DATETIME (UTC) |  | The date and time at which the bundled episode was changed. |
| 4 | `HX_USER_ID` | VARCHAR |  | This column stores the unique identifier for the user who performed the changes to the bundled episode. |
| 5 | `HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `HX_COVERAGE_ID` | NUMERIC |  | The unique ID of the coverage that will be billed for the bundled episode. |
| 7 | `HX_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 8 | `HX_SELFPAY_YN` | VARCHAR |  | Indicates whether the guarantor is responsible for the bundled episode's expected payment. |
| 9 | `HX_BPC_ID` | NUMERIC |  | This column stores the unique identifier for the bundled episode terms associated with the bundled episode. The terms are used to define various reimbursement related attributes for a bundled episode. |
| 10 | `HX_BPC_ID_BPC_NAME` | VARCHAR |  | The name of the bundled episode terms record. |
| 11 | `HX_BPC_CSN` | NUMERIC |  | The contact serial number of the bundled episode terms associated with the bundled episode. The terms are used to define various reimbursement related attributes for a bundled episode. |
| 12 | `HX_BILLING_START_DT` | DATETIME |  | The start date from which the services are covered in the bundled episode. |
| 13 | `HX_BILLING_END_DT` | DATETIME |  | The end date until which the services are covered in the bundled episode. |
| 14 | `HX_EXP_TOT_PMT` | NUMERIC |  | The amount of the total expected payment from the responsible party of a bundled episode. |
| 15 | `HX_EXP_HOSP_PMT` | NUMERIC |  | The amount of the total hospital expected payment from the responsible party of a bundled episode. |
| 16 | `HX_EXP_PROF_PMT` | NUMERIC |  | The amount of the total professional expected payment from the responsible party of a bundled episode. This will only be used when a separate professional payment is expected. |
| 17 | `HX_AUTO_CHG_YN` | VARCHAR |  | Set to yes if this bundled episode update was done via a background system update. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

