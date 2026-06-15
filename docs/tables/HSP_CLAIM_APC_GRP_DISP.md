# HSP_CLAIM_APC_GRP_DISP

> Table that holds the display data for each grouping and claim line tuple when Ambulatory Payment Classification (APC) grouping is run through Epic for a claim.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the claim print record associated with a single hospital account/bucket. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `APC_DISP_CLAIM_LINE` | INTEGER |  | This column stores the claim line number this display line for ambulatory payment classification (APC) grouping is aimed at. |
| 4 | `APC_DISP_TEXT` | VARCHAR |  | The display text for the current display line in the detail display for APC grouping by Epic. |
| 5 | `APC_DISP_VALUE` | VARCHAR |  | The dollar amount (or other value) for the current display line in the detail display for APC grouping by Epic. |
| 6 | `APC_DISP_FORMULA` | VARCHAR |  | The formula text for the current display line in the detail display for APC grouping by Epic. |
| 7 | `APC_DISP_PMT_CLASS_GRP_C_NAME` | VARCHAR | org | This column stores the grouping classification this display line is in reference to. Used to handle multiple sets of grouping results. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

