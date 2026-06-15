# CLARITY_MEDICATION

> The CLARITY_MEDICATION table contains high-level information from all the medications for use in your facility.

**Primary key:** `MEDICATION_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 2 | `NAME` | VARCHAR |  | The name of the medication. |
| 3 | `GENERIC_NAME` | VARCHAR |  | The first line of the generic, non-proprietary name for this medication. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

