# PAT_ENC_HOSP_PROB

> The PAT_ENC_HOSP_PROB contains the hospital problems for each hospital encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 2 | `LINE` | INTEGER | PK | The line count for the item |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The contact serial number (CSN) for this encounter. This number is unique across all patients and encounters in the system. |
| 5 | `PROBLEM_LIST_ID` | NUMERIC | FK→ | The unique (LPL) ID for a problem associated with this hospital encounter. |
| 6 | `PRINCIPAL_PROB_YN` | VARCHAR |  | A flag to indicate if this problem is currently marked as the principal hospital problem. |
| 7 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the deployment owner for this contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

