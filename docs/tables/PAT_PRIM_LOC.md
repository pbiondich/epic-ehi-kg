# PAT_PRIM_LOC

> The PAT_PRIM_LOC table contains the Primary Location information for your patients over time.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting’s encryption utility. |
| 2 | `LINE` | INTEGER | PK | The line number used to identify each line of Primary Location information for the patient. |
| 3 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 4 | `EFF_DATE` | DATETIME |  | The date from which the location is in effect as the member’s Primary Location. |
| 5 | `TERM_DATE` | DATETIME |  | The date after which the location ceases to be the member’s Primary Location. |
| 6 | `CLIN_HX_COMMENTS` | VARCHAR |  | Clinical history comments. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

