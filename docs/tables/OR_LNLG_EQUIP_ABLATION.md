# OR_LNLG_EQUIP_ABLATION

> This table contains information for each pass for other equipment types.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ABLATION_PASS` | INTEGER |  | This item stores which pass the ablation equipment documentation applies to. |
| 4 | `TOT_NUM_PER_PASS` | INTEGER |  | This item stores the number of ablations per pass. |
| 5 | `ENERGY_DENSITY` | NUMERIC |  | This item stores the energy density for this pass. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

