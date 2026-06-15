# ARPB_TX_TEST_INFO

> This table stores the test results for the professional billing procedures.

**Primary key:** `TX_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `HEMATOCRIT_READING` | NUMERIC |  | The hematocrit count of the procedure. This is populated only if the blood related info of the procedure is hematocrit. |
| 3 | `HEMOGLOBIN_READING` | NUMERIC |  | The hemoglobin count of the procedure. This is populated only if the blood related info of the procedure is hemoglobin. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

