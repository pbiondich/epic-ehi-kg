# ORDER_RX_RPT_HX

> This table is used to extract history of report information for each order. From the table, you could find out when the label is printed.

**Primary key:** `ORDER_MED_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique ID of the medication order (prescription) record. NOTE: This is an internal unique identifier for ORD master file records in this table and cannot be used to link to CLARITY_MEDICATION. |
| 2 | `LINE` | INTEGER | PK | The line number for each report printed for the order. |
| 3 | `REPORT_USER_ID` | VARCHAR |  | The unique identifier of the unique action user. |
| 4 | `REPORT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

