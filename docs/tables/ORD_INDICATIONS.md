# ORD_INDICATIONS

> This table stores the indications of use selected for a medication record.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record. |
| 2 | `LINE` | INTEGER | PK | The line count of associated changes in Indication(s) of Use for the order record. |
| 3 | `INDICATIONS_ID` | NUMERIC |  | The indications of use selected for a medication order. |
| 4 | `INDICATIONS_ID_MEDICAL_COND_NAME` | VARCHAR |  | This contains the name of the medical condition. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

