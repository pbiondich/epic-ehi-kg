# CUST_SERV_TEXT

> This table extracts the communication text for a given Customer Service (NCS) record.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The ID number of the customer service communication record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `TEXT_CUST_SERV` | VARCHAR |  | Documentation for the customer service communication. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

