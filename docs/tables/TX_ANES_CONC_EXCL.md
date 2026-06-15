# TX_ANES_CONC_EXCL

> The TX_ANES_CONC_EXCL table contains information concerning the concurrency exclusion date and times for an anesthesia charge.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique key or identification number for a given transaction. |
| 2 | `LINE` | INTEGER | PK | This column contains the line count for the concurrency period exclusion information in this table. Each piece of concurrency period exclusion information is stored on a separate line, one line for each exclusion. |
| 3 | `START_TIME` | DATETIME (Local) |  | The starting time of the period exclusion in anesthesia concurrency calculation. |
| 4 | `START_DATE` | DATETIME |  | The starting date of the period exclusion in anesthesia concurrency calculation. |
| 5 | `END_TIME` | DATETIME (Local) |  | The ending time of the period exclusion in anesthesia concurrency calculation. |
| 6 | `END_DATE` | DATETIME |  | The ending date of the period exclusion in anesthesia concurrency calculation. |
| 7 | `EXCLUSION_COMMENT` | VARCHAR |  | Comment for the period exclusion in anesthesia concurrency calculation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

