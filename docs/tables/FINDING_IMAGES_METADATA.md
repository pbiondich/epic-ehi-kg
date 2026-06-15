# FINDING_IMAGES_METADATA

> This table contains information associated with each image that is attached to an order and displayed in the Findings activity.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `FNDMETA_DOC_INFO_ID` | VARCHAR |  | The unique DCS ID for findings images metadata for an order. |
| 6 | `SELECTED_YN` | VARCHAR |  | Indicates whether the image is selected by the user for this order. 'Y' indicates that the image is selected by the user for this order. 'N' or NULL indicates that the image is not selected by the user for this order. |
| 7 | `GENRTD_CAPT` | VARCHAR |  | The auto-generated caption for the image from the Findings activity. |
| 8 | `FREETEXT_CAPT` | VARCHAR |  | The free-text caption entered by end users for the image from the Findings activity. |
| 9 | `BODY_LOC_RECORD_ID` | NUMERIC |  | The unique ID of the image body location chosen by end users from the Findings activity for the order. |
| 10 | `BODY_LOC_RECORD_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 11 | `IMG_DISP_LABEL` | VARCHAR |  | The unique, auto-generated label ID in the form of a capital letter, which is added in ascending order (A, B, C, etc.). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

