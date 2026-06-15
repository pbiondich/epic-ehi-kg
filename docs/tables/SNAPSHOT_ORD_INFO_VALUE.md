# SNAPSHOT_ORD_INFO_VALUE

> This table has the values for individual data elements that were stored at the time of discharge or when the patient's After Visit Summary was printed. The keys identifying the elements are in the SNAPSHOT_ORDER_DATA table.

**Primary key:** `EVENT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the discharge reconciliation event record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated snapshot data key for this value. Together with EVENT_ID, this forms the foreign key to the SNAPSHOT_ORDER_DATA table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the parts of the value that was stored in the snapshot. |
| 4 | `SNAPSHOT_ORD_VALUE` | VARCHAR |  | One line of the value that was stored in the snapshot. All lines of this data element (that is, all lines with the same EVENT_ID and GROUP_LINE values) should be concatenated to get the full value. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |

