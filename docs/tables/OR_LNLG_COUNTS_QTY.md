# OR_LNLG_COUNTS_QTY

> Clarity table created for storing the related items which are the individual items and their quantities.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `COUNT_IND_ITM_TYP_C_NAME` | VARCHAR | org | This will be used to build the category list of individual items for the counts. |
| 3 | `QUANTITY_COUNTED` | INTEGER |  | This will be used to document the quantity for each individual item counted |
| 4 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

