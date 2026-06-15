# LN_AUTH_OTH_PYR_ID

> This table holds identifiers to identify the payor for which the prior authorization numbers apply. The LN_AUTH_NUM and LN_AUTH_OTH_PYR_ID tables are related to one another. The number of lines in these tables will always be the same and values on the same line in each table will correspond to one another.

**Primary key:** `RECORD_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this contact. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this contact. |
| 4 | `LN_AUTH_OTH_PYR_ID` | VARCHAR |  | This item holds the other payor identifier for the authorization number on the line. The values in this item match the values in the OTH_PYR_ID column of the OTH_CVG_INFO table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

