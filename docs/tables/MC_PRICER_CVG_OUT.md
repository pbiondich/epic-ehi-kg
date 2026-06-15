# MC_PRICER_CVG_OUT

> This table contains coverage information from Local Coverage Determination (LCD) and National Coverage Determination (NCD) checks calculated from the Epic Pricer.

**Primary key:** `PRICER_MSG_ID`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRICER_MSG_ID` | NUMERIC | PK shared | The unique identifier for the Epic Pricer message record. |
| 2 | `CONTRACTOR_NUM` | VARCHAR |  | Contractor number from the Epic Pricer's coverage determination output. |
| 3 | `CONTRACTOR_TYPE_C_NAME` | VARCHAR |  | Contractor type from the Epic Pricer's coverage determination output. |
| 4 | `REVIEW_NEEDED_YN` | VARCHAR |  | Is Review Needed flag from the Epic Pricer's coverage determination output. |
| 5 | `NOT_COVERED_YN` | VARCHAR |  | Is There Not Covered flag from the Epic Pricer's coverage determination output. |
| 6 | `LCD_CHECK_RESULT_C_NAME` | VARCHAR |  | LCD Check Result from the Epic Pricer's coverage determination output. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

