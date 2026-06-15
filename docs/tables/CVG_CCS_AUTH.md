# CVG_CCS_AUTH

> Table to extract California Children's Services (CCS) authorization information.

**Primary key:** `CVG_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK FK→ | The unique ID assigned to the coverage record. This ID may be encrypted if you have elected to use enterprise reporting’s encryption utility. |
| 2 | `LINE` | INTEGER | PK | The line number used to identify each row of California Children's Services (CCS) authorization information for a coverage record. |
| 3 | `CCS_AUTH_NUM` | VARCHAR |  | Stores the Authorization Numbers for California Children's Services (CCS). |
| 4 | `CCS_EFF_FROM_DT` | DATETIME |  | Stores the effective from date for a California Children's Services (CCS) Authorization Number. |
| 5 | `CCS_EFF_TO_DT` | DATETIME |  | Stores the effective to date for a California Children's Services (CCS) Authorization Number. |
| 6 | `CCS_AUTH_PROV` | VARCHAR |  | Stores the authorized provider for a given California Children's Services (CCS) Authorization Number. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |

