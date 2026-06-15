# SMRTDTA_ELEM_CUST_SERVICE

> This table is a bridge between CRM context SmartData element values and the source customer relationship management records.

**Primary key:** `HLV_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLV_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the value record. |
| 2 | `COMM_ID` | NUMERIC | shared | The unique ID of the linked customer relationship management record that is associated with the SmartData element value. |
| 3 | `ELEMENT_ID` | VARCHAR | FK→ | The SmartData identifier (SDI) for this row. |
| 4 | `CUR_VALUE_DATETIME` | DATETIME (Local) |  | The date and time when the SmartData element value was entered by a user through a SmartForm, SmartTool or other documentation tool that files discrete data to SmartData elements. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ELEMENT_ID` | [OR_PNDS](OR_PNDS.md) | sole_pk | high |

