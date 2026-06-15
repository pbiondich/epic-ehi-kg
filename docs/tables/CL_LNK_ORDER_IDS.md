# CL_LNK_ORDER_IDS

> The CL_LNK_ORDER_IDS table contains the overtime related information about the linked group.

**Primary key:** `LNK_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LNK_ID` | NUMERIC | PK FK→ | The unique ID for the linked order group. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `ORD_ID` | NUMERIC |  | The unique identifier of the order records in this linked order group record. |
| 6 | `OFFSET` | INTEGER |  | This item stores the offset interval (in seconds) between linked orders in this group. |
| 7 | `ANCHOR_ORD_ID` | NUMERIC |  | The order whose schedule this order is anchored to |
| 8 | `ANCHOR_DUE_TIME` | NUMERIC |  | Which due time of the anchor order is this order anchored to? If blank, but LNK-70 is set, then this order occurs with every instance of the anchor order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `LNK_ID` | [CL_LNK_ORDERS](CL_LNK_ORDERS.md) | sole_pk | high |

