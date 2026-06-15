# OTH_PYR_BP_SEC_ID

> This table holds additional IDs used to identify the billing provider to the other payor. The OTH_PYR_BP_SEC_QUA and OTH_PYR_BP_SEC_ID tables are related to one another. The number of lines in these tables will always be the same and values on the same line in each table will correspond to one another.

**Primary key:** `RECORD_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this contact. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this contact. |
| 4 | `OTH_PYR_BP_SEC_ID` | VARCHAR |  | This item holds the billing provider secondary ID for the other payer. It is used on both electronic and paper claims. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

