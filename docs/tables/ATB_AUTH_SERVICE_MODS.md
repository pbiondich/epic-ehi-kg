# ATB_AUTH_SERVICE_MODS

> This table contains the modifiers for the service line procedure information.

**Primary key:** `AUTH_BUNDLE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the Auth Bundle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUTH_MODIFIER_ID` | VARCHAR |  | The unique ID of the Modifiers associated with the Auth Bundle service's procedure information. |
| 4 | `AUTH_MODIFIER_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

