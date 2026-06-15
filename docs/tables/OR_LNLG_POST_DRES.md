# OR_LNLG_POST_DRES

> This line IDs (ORM) table contains information about dressings used after a surgery during the post-op phase to include the specific supply and the quantity used.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line (ORM) record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `POST_OP_DRSG_SUP_ID` | VARCHAR |  | Specifies the multiple dressings used for a particular incision site and laterality. |
| 4 | `POST_OP_DRSG_SUP_ID_SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |
| 5 | `POST_OP_DRSNG_QTY` | INTEGER |  | Quantity of the related dressing used. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

