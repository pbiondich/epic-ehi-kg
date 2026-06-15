# ARPB_PNB_RULE_OVERRIDES

> This table contains information on all the Posted Not Billed rules that have been overridden by users.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PNB_OVRIDE_RULE_ID` | VARCHAR |  | This item stores Posted Not Billed rules that have been overidden. |
| 4 | `PNB_OVRIDE_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 5 | `PNB_OVRIDE_USER_ID` | VARCHAR |  | This item stores Posted Not Billed rule overriding user. |
| 6 | `PNB_OVRIDE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `PNB_OVRIDE_INST_UTC_DTTM` | DATETIME (UTC) |  | This item stores Posted Not Billed rule overriding instant in UTC. |
| 8 | `PNB_OVRIDE_COMMENT` | VARCHAR |  | This item stores Posted Not Billed rule override comment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

