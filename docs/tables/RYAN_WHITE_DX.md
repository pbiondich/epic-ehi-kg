# RYAN_WHITE_DX

> This table contains diagnosis information from Ryan White abstractions.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RYN_WHT_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `RYN_WHT_DX_DATE` | DATETIME |  | Start date of a diagnosis documented on the patient for Ryan White reporting. |
| 5 | `RYN_WHT_DX_RESOLVED_DATE` | DATETIME |  | End date of a diagnosis documented on the patient for Ryan White reporting. |
| 6 | `RYN_WHT_DX_ASSESSMENT_C_NAME` | VARCHAR |  | Assessment detail for a diagnosis documented on the patient for Ryan White reporting. |
| 7 | `RYN_WHT_DX_COMMENT` | VARCHAR |  | Additional comment for a diagnosis documented on the patient for Ryan White reporting. |
| 8 | `RYN_WHT_DX_PROBLEM` | VARCHAR |  | Medical issue resulting in diagnosis documented on the patient for Ryan White reporting. |
| 9 | `RYN_WHT_DX_STATUS_C_NAME` | VARCHAR |  | Status category for a diagnosis documented on the patient for Ryan White reporting. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

