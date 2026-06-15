# PC_FEEDBACK

> Contains feedback related to the Potential Condition nodes on a hospital account.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PC_RELATED_CODE_YN` | VARCHAR |  | Determines if a code related to the Potential Condition is on the hospital account. |
| 4 | `PC_RELATED_QUERY_YN` | VARCHAR |  | Determines if a query type related to the Potential Condition is on the hospital account. |
| 5 | `PC_AI_QRY_EVIDENCE_ENABLED_YN` | VARCHAR |  | Indicates whether the potential condition is enabled to display evidence from the AI query model when the potential condition first appears on the hospital account, meaning both the potential condition's condition is enabled for AI and the potential condition's report includes the AI evidence print group LPG 38085. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

