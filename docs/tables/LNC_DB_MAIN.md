# LNC_DB_MAIN

> This is the primary table for Logical Observation Identifiers Names and Codes (LOINC®) information.

**Primary key:** `RECORD_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID_LNC_LONG_NAME` | VARCHAR |  | The more readable format than the fully specified name in Logical Observation Identifiers Names and Codes (LOINC®) code. |
| 2 | `LNC_CODE` | VARCHAR |  | The unique code for the Logical Observation Identifiers Names and Codes (LOINC®) code. |
| 3 | `LNC_LONG_NAME` | VARCHAR |  | The more readable format than the fully specified name in Logical Observation Identifiers Names and Codes (LOINC®) code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

