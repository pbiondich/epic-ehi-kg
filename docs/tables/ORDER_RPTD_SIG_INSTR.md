# ORDER_RPTD_SIG_INSTR

> For each row in ORDER_RPTD_SIG_HX, this table contains the free-text instructions that were entered, if any.

**Primary key:** `ORDER_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with the instructions for this medication. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of instructions within this record. |
| 4 | `INSTRUCTIONS` | VARCHAR |  | The additional instructions included with the medication instructions. |
| 5 | `MED_USE_IDENT` | VARCHAR |  | This item stores the MGB ID for MP9. |
| 6 | `MED_USE_UTC_DTTM` | DATETIME (UTC) |  | This is the effective instant of the medication use. |
| 7 | `MED_USE_PERIOD` | INTEGER |  | This stores the period (amount of time in seconds) of a medication use. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

