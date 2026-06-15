# CAP_PAY_EFF_PERIODS

> This table includes information about member effective periods for outgoing PCP and non-member list-using specialty capitation transactions.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier of the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MEMBER_EFF_DATE` | DATETIME |  | The member's effective dates on the coverage that were used to pay the capitation. |
| 4 | `MEMBER_TERM_DATE` | DATETIME |  | The member's termination dates on the coverage that were used to pay capitation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

