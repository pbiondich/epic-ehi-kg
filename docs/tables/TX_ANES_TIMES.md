# TX_ANES_TIMES

> The TX_ANES_TIMES table contains information concerning the date and times for an anesthesia charge.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique key or identification number for a given transaction. |
| 2 | `LINE` | INTEGER | PK | This column contains the line count for the information in this table. Each anesthesia time/date range is stored on a separate line, one line for each range. |
| 3 | `START_TIME` | DATETIME (Local) |  | Start time of the anesthesia procedure. |
| 4 | `START_DATE` | DATETIME |  | Start date of the anesthesia procedure. |
| 5 | `END_TIME` | DATETIME |  | End time of the anesthesia procedure. |
| 6 | `END_DATE` | DATETIME |  | End date of the anesthesia procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

