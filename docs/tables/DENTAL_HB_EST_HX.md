# DENTAL_HB_EST_HX

> Dental procedure estimates history as calculated from the Hospital Billing (HB) estimates application programming interface (API).

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DENT_HX_CALC_PRICE` | NUMERIC |  | The historical price of a dental procedure as calculated by the Hospital Billing application |
| 4 | `DENT_HX_ADJ_PRICE` | NUMERIC |  | The historical user-adjusted price of the dental procedure (Hospital Billing estimates only) |
| 5 | `DENT_HX_ADJ_REASN_C_NAME` | VARCHAR | org | The historical reason for a price adjustment for a dental procedure (Hospital Billing estimates only) |
| 6 | `DENT_HX_ADJ_COMMENT` | VARCHAR |  | The historical comment for the price adjustment for a dental procedure (Hospital Billing estimates only) |
| 7 | `DENT_HX_ADJ_USER_ID` | VARCHAR |  | Historical user that adjusted the estimate (Hospital Billing estimates only) |
| 8 | `DENT_HX_ADJ_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `DENT_HX_PAT_PORTION` | NUMERIC |  | Stores the historical patient portion of a dental procedure's price (used for Hospital Billing estimates only) |
| 10 | `DENT_HX_OUTDATED_YN` | VARCHAR |  | Stores whether a historical estimate value is flagged as out of date (used for Hospital Billing estimates only) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

