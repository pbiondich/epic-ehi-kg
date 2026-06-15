# ACCT_GUAR_PAT_INFO

> This table contains information about the account guarantor - patient relationship.

**Primary key:** `ACCOUNT_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | NUMERIC | PK FK→ | The unique ID for the account. This ID number could by encrypted if you have elected to implement enterprise reporting’s encryption security function. |
| 2 | `LINE` | INTEGER | PK | Line number to uniquely identify the patient within the guarantor account. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID for the patient related to the guarantor of the account. |
| 4 | `GUAR_REL_TO_PAT_C_NAME` | VARCHAR | org | The relationship of the patient to the guarantor of the account (e.g. Mother, Brother, Legal Guardian, etc.) |
| 5 | `PATIENT_ADDR_LINKED_YN` | VARCHAR |  | Indicates whether the patient address and the guarantor address are linked. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

