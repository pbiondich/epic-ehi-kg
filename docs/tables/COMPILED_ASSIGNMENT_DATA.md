# COMPILED_ASSIGNMENT_DATA

> This table holds the External System Identifier Bundles and roster identifiers for which compiled roster assignment data was loaded.

**Primary key:** `ASGN_DATA_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ASGN_DATA_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the assignment data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this assignment data record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_LOG_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| 4 | `ROSTER_IDENTIFIER_C_NAME` | VARCHAR | org | The roster population that this line contains compiled tracking data for. |
| 5 | `ASSIGNMENT_PERIOD_EFF_DATE` | DATETIME |  | The start date of this compiled roster assignment period. |
| 6 | `ASSIGNMENT_PERIOD_TERM_DATE` | DATETIME |  | The end date of this compiled roster assignment period. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ASGN_DATA_ID` | [ASSIGNMENT_DATA](ASSIGNMENT_DATA.md) | sole_pk | high |

