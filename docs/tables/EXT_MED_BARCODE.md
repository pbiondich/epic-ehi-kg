# EXT_MED_BARCODE

> This table contains information about accepted barcodes for medication orders from external sources. These barcodes are all valid for barcoded medication administration (BCMA).

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXT_MED_BARCODE_IDENT` | VARCHAR |  | The barcode IDs for the medication order from an external source (e.g., from an external pharmacy through RxFill messages). |
| 4 | `DISP_SOURCE_CONTACT_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. This is the contact date for the dispense on the order that sent over this external medication barcode. If empty, the dispense that sent over this external medication barcode is on a previous order. |
| 5 | `EXT_BARCODE_SOURCE_C_NAME` | VARCHAR | org | Stores the source category of this external barcode. |
| 6 | `EXT_BARCODE_SOURCE_ORDER_ID` | NUMERIC |  | Stores the source order ID if this external barcode is copied from another order. |
| 7 | `EXT_BARCODE_ADDED_USER_ID` | VARCHAR |  | Stores the user that added this barcode to the order. |
| 8 | `EXT_BARCODE_ADDED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `EXT_BARCODE_ADDED_UTC_DTTM` | DATETIME (UTC) |  | Stores the UTC instant when this external barcode is added to the order. |
| 10 | `EXT_BARCODE_BEFORE_REMOVED` | VARCHAR |  | Stores the original external barcode if it has been removed from the order. |
| 11 | `EXT_BARCODE_REMOVE_RSN_C_NAME` | VARCHAR | org | Stores the reason of removal if this external barcode has been removed from the order. |
| 12 | `EXT_BARCODE_REMOVE_USER_ID` | VARCHAR |  | Stores the user that removed this external barcode from the order. |
| 13 | `EXT_BARCODE_REMOVE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 14 | `EXT_BARCODE_REMOVE_UTC_DTTM` | DATETIME (UTC) |  | Stores the UTC instant when this external barcode is removed from the order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

