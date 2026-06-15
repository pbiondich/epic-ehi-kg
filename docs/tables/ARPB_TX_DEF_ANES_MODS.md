# ARPB_TX_DEF_ANES_MODS

> System default anesthesia modifiers for anesthesia charges.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ANES_DEFAULT_MOD` | VARCHAR |  | Returns a system default anesthesia modifier for this charge. This is derived from the charge's concurrency, providers, and settings found in the payor with standard anesthesia modifier settings (I EAF 8161). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

