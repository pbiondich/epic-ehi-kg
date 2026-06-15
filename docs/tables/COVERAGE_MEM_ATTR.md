# COVERAGE_MEM_ATTR

> The COVERAGE_MEM_ATTR table contains a list of coverage attributes assigned to members on coverages.

**Primary key:** `COVERAGE_ID`, `LINE`, `PAT_ID`, `ATTR_LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique ID assigned to the coverage record. This ID may be encrypted if you have elected to use enterprise reporting’s encryption utility. |
| 2 | `LINE` | INTEGER | PK | The line count for patients on the coverage. |
| 3 | `PAT_ID` | VARCHAR | PK FK→ | The unique patient ID for each line on the coverage. |
| 4 | `ATTR_LINE` | INTEGER | PK | The line number used to identify each attribute for a patient. |
| 5 | `CVG_ATTR_C` | INTEGER |  | The coverage attribute attached to the member/coverage combination. |
| 6 | `EFF_DATE` | DATETIME |  | The effective date of the coverage attribute for the member on the coverage. |
| 7 | `TERM_DATE` | DATETIME |  | The termination date of the coverage attribute for the member on the coverage. |
| 8 | `COMMENTS` | VARCHAR |  | The free text comment associated with the coverage attribute for the member on the coverage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

