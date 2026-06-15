# ORD_AUD_BILLING_MODS

> This table contains audit information about the modifiers associated with an imaging order which will impact downstream billing.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BILLING_MODIFIERS` | VARCHAR |  | Audit information about modifiers (category values) that will satisfy billing requirements. The values are delimited by "^". The source item is located at ORDER_RAD_MODS.MODIFIER_ID. |
| 4 | `BILLING_MODIFIERS_EXT_VALS` | VARCHAR |  | Audit information about modifiers (external category values) that will satisfy billing requirements. The values are delimited by "^". The source item is located at ORDER_RAD_MODS.MODIFIER_ID. This column shows the translated external value as of when the column was last extracted. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

