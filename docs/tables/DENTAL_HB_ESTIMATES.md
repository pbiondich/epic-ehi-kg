# DENTAL_HB_ESTIMATES

> Dental procedure estimates as calculated from the Hospital Billing (HB) estimates application programming interface (API).

**Primary key:** `FINDING_ID`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `DENTAL_CALC_PRICE` | NUMERIC |  | The price of a dental procedure as calculated by the Hospital Billing application |
| 3 | `DENTAL_ADJ_PRICE` | NUMERIC |  | The user-adjusted price of the dental procedure (Hospital Billing estimates only) |
| 4 | `DENTAL_ADJ_REASON_C_NAME` | VARCHAR | org | The reason for a price adjustment for a dental procedure (Hospital Billing estimates only) |
| 5 | `DENTAL_ADJ_COMMENT` | VARCHAR |  | The comment for the price adjustment for a dental procedure (Hospital Billing estimates only) |
| 6 | `DENTAL_ADJ_USER_ID` | VARCHAR |  | The user that adjusted the estimate (Hospital Billing estimates only) |
| 7 | `DENTAL_ADJ_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `DENTAL_PAT_PORTION` | NUMERIC |  | The patient portion of a dental procedure's price (used for Hospital Billing estimates only) |
| 9 | `DENTAL_OUTDATED_YN` | VARCHAR |  | Stores whether the current estimate value is flagged as out of date and needs to be recalculated (used for Hospital Billing estimates only) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

