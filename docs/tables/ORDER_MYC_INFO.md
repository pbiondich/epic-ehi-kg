# ORDER_MYC_INFO

> When sharing a lab result with a web-based chart system patient, the clinician may choose to attach a Result Comment. Data for the Result Comment patient note is stored in this table.

**Primary key:** `ORDER_PROC_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record that is being released/unreleased. |
| 2 | `RELEASED_YN` | VARCHAR |  | Whether a result is released to a patient on MyChart. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

