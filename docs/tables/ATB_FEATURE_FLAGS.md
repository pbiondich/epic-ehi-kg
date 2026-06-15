# ATB_FEATURE_FLAGS

> ATB Feature Flags.

**Primary key:** `AUTH_BUNDLE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the authorization bundle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FEATURE_FLAGS_C_NAME` | VARCHAR |  | The feature flags for the ATB, helps determine if data is not set because it was null or because it wasn't implmented yet. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

