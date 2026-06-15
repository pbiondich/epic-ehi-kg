# PAYER_PROXY_REQ

> Contains data associated with a Payer Platform Proxy request audit. This includes information such as: the type of request, the source of the request, the network the request was sent over, the destination it was routed to, etc.

**Primary key:** `REQ_AUD_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REQ_AUD_ID` | NUMERIC | PK | The unique identifier (.1 item) for the request record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The patient associated with the request |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

