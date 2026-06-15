# TPL_UPDATE_INFO

> The update information for the treatment plan.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The treatment plan ID. |
| 2 | `LINE` | INTEGER | PK | The line number that corresponds to each update of the treatment plan in this row. |
| 3 | `UPDATED_BY_USER_ID` | VARCHAR |  | The user ID of the person who performed an update of the treatment plan in this row. |
| 4 | `UPDATED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `UPDATED_ON_TM` | DATETIME (Local) |  | The date/time in external format of an update to the treatment plan in this row. |
| 6 | `UPDATED_IN_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Stores the contact serial number (CSN) of a patient visit in which this plan was updated and saved. This item is empty if the update occurred outside of an encounter context. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `UPDATED_IN_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

