# IB_PHRM_ORDER_ID

> The IB_PHRM_ORDER_ID table contains Order IDs attached with an E-Prescribing Sig Map In Basket message.

**Primary key:** `MSG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MSG_ID` | VARCHAR | PK FK→ | The unique identifier of the message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PHRM_ORDER_ID` | NUMERIC |  | Unique identifier of an incoming order from a pharmacy that includes a free text sig with a mapping request for a discrete sig. Such requests are sent when a prescription request message is sent from an e-prescribing pharmacy interface. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MSG_ID` | [IB_MESSAGES](IB_MESSAGES.md) | sole_pk | high |

