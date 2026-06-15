# OR_LNLG_LITHO_STONE_INFO

> This table contains information related to Lithotripsy procedures.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STONE_SIZE` | NUMERIC |  | This item stores stone size for the lithotripsy procedure. |
| 4 | `STONE_LOCATION_C_NAME` | VARCHAR | org | This item stores the stone location for the lithotripsy procedure |
| 5 | `NUM_OF_SHOCKS` | INTEGER |  | This item stores the number of shocks applied during the lithotripsy procedure. |
| 6 | `STONE_DENSITY_C_NAME` | VARCHAR | org | This item stores the stone density for the lithotripsy procedure. |
| 7 | `POWER_INDEX` | NUMERIC |  | This item stores the power index (in kV) for the lithotripsy procedure. |
| 8 | `GATED_SHOCKS` | NUMERIC |  | This item stores the calculated gated shocks for the lithotripsy procedure. The gated shocks value is the product of the number of shocks and the power index. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

