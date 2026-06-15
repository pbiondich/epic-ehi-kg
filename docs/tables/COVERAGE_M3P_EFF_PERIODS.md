# COVERAGE_M3P_EFF_PERIODS

> Clarity table for a coverage's M3P effective period information.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `M3P_EFF_ELECT_UTC_DTTM` | DATETIME (UTC) |  | The date and time that a Medicare Advantage member elects to enroll in the Medicare Prescription Payment Plan. |
| 4 | `M3P_EFF_DATE` | DATETIME |  | The date when the member begins their Medicare Prescription Payment Plan. |
| 5 | `M3P_TERM_DATE` | DATETIME |  | The date when the member ends their Medicare Prescription Payment Plan. |
| 6 | `M3P_TERM_CODE_C_NAME` | VARCHAR |  | The Termination Reason Code category ID for the Medicare Prescription Payment Plan effective period. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

