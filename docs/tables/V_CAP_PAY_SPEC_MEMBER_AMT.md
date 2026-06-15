# V_CAP_PAY_SPEC_MEMBER_AMT

> Contains specialty amounts of capitation payments, matched to the associated members.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The internal ID of the transaction. |
| 2 | `LINE` | INTEGER | PK | The line number in the associated member list for this transaction. |
| 3 | `MEMBER_ID` | VARCHAR |  | The ID of the associated member for this transaction. |
| 4 | `SPEC_CAP_AMT` | NUMERIC |  | The specialty rate of the associated member in this transaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

