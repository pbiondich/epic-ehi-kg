# OR_IMP_SKNSUB

> This stores the documentation for skin substitute implants.

**Primary key:** `IMPLANT_ID`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the implant record. |
| 2 | `IMP_WOUND_TYPE_C_NAME` | VARCHAR | org | Type of wound on which skin substitute is applied to |
| 3 | `SKINSUB_NUMBER_TIMES_APPLIED` | INTEGER |  | Number of times skin substitute is applied |
| 4 | `SKINSUB_WOUND_SIZE` | NUMERIC |  | Size of wound on which skin substitute is applied to in square centimeters. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

