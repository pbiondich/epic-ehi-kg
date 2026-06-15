# ORDER_MED_ALTCSN

> It contains the unique contact specific alert number for the order. Link it to alert related tables, such as ALT_HISTORY, ALT_ORDINFO, to get alert related information.

**Primary key:** `ORDER_MED_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique ID of the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | The contact date that corresponds to the encounter this order alert occurred. |
| 3 | `LINE` | INTEGER | PK | The line number for each alert unique contact number. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `ALT_CSN_ID` | NUMERIC | FK→ | The unique ID for the alert across all contacts and alerts in ALT master file. You could link this to ALT_HISTORY table to get the alert information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ALT_CSN_ID` | [ALT_HISTORY](ALT_HISTORY.md) | sole_pk | high |
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

