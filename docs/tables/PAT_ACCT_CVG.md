# PAT_ACCT_CVG

> The PAT_ACCT_CVG table contains information about a patient’s accounts and coverages. The table will contain one record for each account for a patient. The record will also contain the patient’s primary coverage for that account.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting’s security utility. |
| 2 | `LINE` | INTEGER | PK | The line number. A patient id can be associated with multiple rows of accounts and coverages. |
| 3 | `ACCOUNT_ID` | NUMERIC | FK→ | The unique account record ID for an account associated with this patient. This ID number may be encrypted if you have elected to use enterprise reporting’s security utility. |
| 4 | `ACCOUNT_TYPE_C_NAME` | VARCHAR | org | Category value associated with the type of account, such as Personal/Family, Worker’s Comp, etc. |
| 5 | `ACCOUNT_ACTIVE_YN` | VARCHAR |  | Is the account active at the time of the extract: Y or N. |
| 6 | `COVERAGE_ID` | NUMERIC | FK→ | The unique ID assigned to the coverage record associated with this patient and account. This ID may be encrypted if you have elected to use enterprise reporting’s encryption utility. |
| 7 | `FIN_CLASS_NAME` | VARCHAR | org | The financial class category number for the patient's primary coverage on the account. If there is no coverage, it is the account's financial class. |
| 8 | `GUAR_PAT_REL_NAME` | VARCHAR | org | Relation between the guarantor and patient. |
| 9 | `ACCT_PRIM_EPSD_ID` | VARCHAR |  | Episode associated with this account. |
| 10 | `ACCT_COMMENT` | VARCHAR |  | Free text comment associated with this account. |
| 11 | `ACCT_PRIM_CLAIM_ID` | NUMERIC |  | The unique system Identifier of the patient's primary Claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

