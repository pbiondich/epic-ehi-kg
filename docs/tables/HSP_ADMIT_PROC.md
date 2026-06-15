# HSP_ADMIT_PROC

> The HSP_ADMIT_PROC table contains information on admission procedures. This table is based on PAT_ENC_CSN_ID.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LINE` | INTEGER | PK | The line number of the admission procedure for this patient. |
| 2 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 3 | `ADMIT_PROC_TEXT` | VARCHAR |  | Free text admission procedure for the patient. |
| 4 | `ADMIT_PROC_DATE` | DATETIME |  | The date that the admission procedure is scheduled for the patient. |
| 5 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 6 | `ADM_PXDX_ASSOC` | VARCHAR |  | Used for ABN checks. A comma delimited list of line numbers that associate this procedure to a diagnosis. |
| 7 | `ADM_PX2ABN_LINK` | VARCHAR |  | A comma-delimited list of line numbers that indicate which ABN's are associated with this procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

