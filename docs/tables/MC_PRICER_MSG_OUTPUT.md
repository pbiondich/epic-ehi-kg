# MC_PRICER_MSG_OUTPUT

> This table contains core CMS message output data from the Epic Pricer.

**Primary key:** `PRICER_MSG_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRICER_MSG_ID` | NUMERIC | PK shared | The unique identifier for the Epic Pricer message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MSG_OUT_NAME` | VARCHAR |  | Node name for JSON representation of Epic Pricer output message. |
| 4 | `MSG_OUT_VAL` | VARCHAR |  | Node value for JSON representation of Epic Pricer output message. |
| 5 | `MSG_OUT_PARENT` | INTEGER |  | Parent node for JSON representation of Epic Pricer output message. |
| 6 | `MSG_OUT_MC_NODE_TYPE_C_NAME` | VARCHAR |  | Node type for JSON representation of Epic Pricer output message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

