# AGENT_STATE_LICENSE_NUMS

> The table that stores information for State License Numbers (SLNs). Including the SLN, State, Eff date, Term Date.

**Primary key:** `AGENT_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AGENT_ID_AGENT_NAME` | VARCHAR |  | The name of the agent. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REVISED_LICENSED_TAX_STATE_C_NAME` | VARCHAR | org | Agent's SLN State |
| 4 | `LICENSE_EFF_DATE` | DATETIME |  | Agent State License Number Effective Date |
| 5 | `LICENSE_TERM_DATE` | DATETIME |  | Agent's State License Number Termination Date |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

