# ODC_USER_CTX_OWNER

> The ODC_USER_CTX_OWNER table contains the user created context owner information for the order context record.

**Primary key:** `ORDER_CONTEXT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_CONTEXT_ID` | NUMERIC | PK FK→ | The unique identifier for the order context record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `USER_CTX_OWNER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_CONTEXT_ID` | [ODC_BASIC](ODC_BASIC.md) | sole_pk | high |

