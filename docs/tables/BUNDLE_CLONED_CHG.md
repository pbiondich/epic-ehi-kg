# BUNDLE_CLONED_CHG

> This table contains cloned charges that are created from this charge record.

**Primary key:** `CHARGE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CHARGE_ID` | NUMERIC | PK | The unique identifier (.1 item) for the charge line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLONED_CHARGE_ID` | NUMERIC |  | Points to the cloned charge records for this charge. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

