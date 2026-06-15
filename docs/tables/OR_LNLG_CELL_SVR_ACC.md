# OR_LNLG_CELL_SVR_ACC

> Contains related group cell saver accessory information.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXP_DATE` | DATETIME |  | The expiration date of the cell saver accessory. |
| 4 | `MODEL` | VARCHAR |  | The model of the cell saver accessory. |
| 5 | `ACCESSORY_TYPE_C_NAME` | VARCHAR | org | The type of cell saver accessory category number. |
| 6 | `LOT_NUM` | VARCHAR |  | The lot number of the cell saver accessory. |
| 7 | `QUANTITY` | INTEGER |  | The quantity of the cell saver accessory. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

