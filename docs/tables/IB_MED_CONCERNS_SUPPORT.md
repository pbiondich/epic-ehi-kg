# IB_MED_CONCERNS_SUPPORT

> Stores the support pool that the message was re-routed to.

**Primary key:** `MSG_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MSG_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the in basket message record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `SUPPORT_IB_POOL_ID` | NUMERIC |  | Stores the supporting pool that the Medication Concern message was routed to for the recipient listed in I EOW 795. |
| 5 | `SUPPORT_IB_POOL_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MSG_ID` | [IB_MESSAGES](IB_MESSAGES.md) | sole_pk | high |

