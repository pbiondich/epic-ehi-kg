# CLP_MEA_INFO

> This table contains test result information (e.g. hematocrit readings, hemoglobin readings etc.) from the claim print record.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | Claim record ID. |
| 2 | `LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 3 | `MEA_TEST_C_NAME` | VARCHAR | org | This is the measurement result qualifier. |
| 4 | `MEA_RESULT` | NUMERIC |  | This is the measurement result value. |
| 5 | `MEA_IDENTIFIER_C_NAME` | VARCHAR | org | Measurement identifier. |
| 6 | `MEA_LINE_INDEX` | NUMERIC |  | This contains a line number that corresponds to the claim line the measurement result is related to. |
| 7 | `MEA_TEST_DATE` | DATETIME |  | This is the measurement performed date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

