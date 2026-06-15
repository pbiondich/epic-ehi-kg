# LINKED_MULT_ASGN

> This table contains the linked child transport request records (TNP) associated with multiple transporter assignment.

**Primary key:** `TRANSPORT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TRANSPORT_ID` | NUMERIC | PK FK→ | The unique identifier for the request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LINKED_MULT_ASGN_ID` | NUMERIC |  | This item contains the linked transport requests for any additional transporters that are needed for a request. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `TRANSPORT_ID` | [TXPORT_REQ_INFO](TXPORT_REQ_INFO.md) | sole_pk | high |

