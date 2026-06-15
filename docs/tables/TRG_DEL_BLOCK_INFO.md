# TRG_DEL_BLOCK_INFO

> The information about the deleted order blocks (patient order templates) in the treatment day.

**Primary key:** `REGIMEN_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGIMEN_ID` | NUMERIC | PK shared | The unique identifier for the patient order group record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DT` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `DELETED_BLOCK_ID` | NUMERIC |  | Stores the deleted order id. |
| 6 | `DELETED_BLOCK_CAT_C_NAME` | VARCHAR | org | Stores the category of the block. |
| 7 | `DEL_BLK_SRC_DAY_UID` | VARCHAR |  | Stores the unique ID of the day from which it was created. |
| 8 | `DEL_ORD_SRC_AOG_ID` | NUMERIC |  | This column holds the order template (OTP) ID of the advanced order group order (if any) from which this deleted order was created. |
| 9 | `DELETED_SOURCE_OTP_ID` | NUMERIC |  | Stores the block source (I TRG 110) for a deleted order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

