# MYC_MESG_ORD_ITEMS

> Holds a list of order IDs that are used in renewal request messaging.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The ID of the web-based chart system message record. |
| 2 | `LINE` | INTEGER | PK | Line number for the current order ID. |
| 3 | `REN_REQ_ORDER_ID` | NUMERIC |  | The order ID of the medication being requested for renewal. |
| 4 | `REN_REQ_FILL_SOURCE_C_NAME` | VARCHAR |  | Stores the source for the refill request. Default is 2-Web |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

