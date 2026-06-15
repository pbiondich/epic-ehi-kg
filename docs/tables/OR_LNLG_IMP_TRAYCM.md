# OR_LNLG_IMP_TRAYCM

> This table contains the Implant Tray Component information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `LINE` | INTEGER | PK | The line number of the component record |
| 3 | `TRAY_COMP_ORIG_NUM` | INTEGER |  | This item stores the original number of components of this inventory item type which were present in the tray. |
| 4 | `TRAY_COMP_SUP_KEY` | VARCHAR |  | This item stores a key containing the unique tray number and inventory item. |
| 5 | `TRAY_COMP_ORM_ID` | VARCHAR |  | The pointer to the implant row record for this tray component. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

