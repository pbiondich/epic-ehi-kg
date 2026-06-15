# OR_LNLG_COUNTS

> This table contains the Counts information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 24  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the Line (ORM) record |
| 2 | `COUNT_XRAY_YN` | VARCHAR |  | Indicates whether or not an X-ray was performed for this count record. Y indicates the X-ray was used, while N indicates that the X-ray was not used. This item may be set in the event of an incorrect count, therefore it could be null, usually indicating a correct count. |
| 3 | `COUNT_MD_NTFD_YN` | VARCHAR |  | Indicates whether or not the physician was notified for this count record. Y indicates the physician was notified, while N indicates that the physician was not notified. This item may be set in the event of an incorrect count, therefore it could be null, usually indicating a correct count. |
| 4 | `COUNT_INST_DTTM` | DATETIME (Local) |  | The instant the count was taken. |
| 5 | `COUNT_PERFORMD_DTTM` | DATETIME (Local) |  | This item stores the time when a count is performed. |
| 6 | `COUNT_MD_NOTIFIED_DTTM` | DATETIME (UTC) |  | This column stores when the physician was notified during an incorrect count. |
| 7 | `COUNT_XRAY_TAKEN_DTTM` | DATETIME (UTC) |  | This column stores when the X-ray was taken during a count. |
| 8 | `COUNT_ALL_CLEAR_DTTM` | DATETIME (UTC) |  | This column stores the time when all clear was called as part of a count. |
| 9 | `COUNTS_ITEM1_C_NAME` | VARCHAR | org | Stores the item being counted in the current count. This is a category list value. |
| 10 | `COUNTS_ITEM1_FREE_TEXT` | VARCHAR |  | Stores the item being counted in the current count. This is intended to be used if a user selects "other" as the category list value. |
| 11 | `COUNTS_ITEM1_TOTAL` | INTEGER |  | The total of this type of item that was counted. |
| 12 | `COUNTS_ITEM2_C_NAME` | VARCHAR |  | Stores the item being counted in the current count. This is a category list value. |
| 13 | `COUNTS_ITEM2_FREE_TEXT` | VARCHAR |  | Stores the item being counted in the current count. This is intended to be used if a user selects "other" as the category list value. |
| 14 | `COUNTS_ITEM2_TOTAL` | INTEGER |  | The total of this type of item that was counted. |
| 15 | `COUNTS_ITEM3_C_NAME` | VARCHAR |  | Stores the item being counted in the current count. This is a category list value. |
| 16 | `COUNTS_ITEM3_FREE_TEXT` | VARCHAR |  | Stores the item being counted in the current count. This is intended to be used if a user selects "other" as the category list value. |
| 17 | `COUNTS_ITEM3_TOTAL` | INTEGER |  | The total of this type of item that was counted. |
| 18 | `COUNTS_ITEM4_C_NAME` | VARCHAR |  | Stores the item being counted in the current count. This is a category list value. |
| 19 | `COUNTS_ITEM4_FREE_TEXT` | VARCHAR |  | Stores the item being counted in the current count. This is intended to be used if a user selects "other" as the category list value. |
| 20 | `COUNTS_ITEM4_TOTAL` | INTEGER |  | The total of this type of item that was counted. |
| 21 | `COUNTS_ITEM5_C_NAME` | VARCHAR |  | Stores the item being counted in the current count. This is a category list value. |
| 22 | `COUNTS_ITEM5_FREE_TEXT` | VARCHAR |  | Stores the item being counted in the current count. This is intended to be used if a user selects "other" as the category list value. |
| 23 | `COUNTS_ITEM5_TOTAL` | INTEGER |  | The total of this type of item that was counted. |
| 24 | `NUMBER_OF_RECOUNTS` | INTEGER |  | This column stores the number of recounts done. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

