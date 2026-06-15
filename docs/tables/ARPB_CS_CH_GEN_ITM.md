# ARPB_CS_CH_GEN_ITM

> Transaction Charge Generic Items. These items are usually entered manually by users in charge entry, and are stored in the temporary accounts receivable (TAR) record. These items are customizable, so their use and meaning are defined by an administrator in the Professional Billing Profile. The backend items are not available to users for entry. Contact your administrator or Epic representative to find out their meaning. Note: TAR records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table might be lost if you truncate the table.

**Primary key:** `TAR_ID`  
**Columns:** 27  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique ID of a temporary transaction record. This represents an individual charge session. |
| 2 | `DATE_ITEM_1_DT` | DATETIME |  | The value of charge generic date item 1 in the charge session (TAR) record. The information is entered by users when the charge is posted in Charge Entry. |
| 3 | `DATE_ITEM_2_DT` | DATETIME |  | The value of charge generic date item 2 in the charge session (TAR) record. The information is entered by users when the charge is posted in Charge Entry. |
| 4 | `CATEGORY_ITEM_1_C_NAME` | VARCHAR | org | The value of charge generic category item 1 in the charge session (TAR) record. The information is entered by users when the charge is posted in Charge Entry. The category values are all custom values that can be viewed or entered by Administrators. |
| 5 | `CATEGORY_ITEM_2_C_NAME` | VARCHAR | org | The value of charge generic category item 2 in the charge session (TAR) record. The information is entered by users when the charge is posted in Charge Entry. The category values are all custom values that can be viewed or entered by Administrators. |
| 6 | `CATEGORY_ITEM_3_C_NAME` | VARCHAR | org | The value of charge generic category item 3 in the charge session (TAR) record. The information is entered by users when the charge is posted in Charge Entry. The category values are all custom values that can be viewed or entered by Administrators. |
| 7 | `STRING_ITEM_1` | VARCHAR |  | The value of charge generic string item 1 in the charge session (TAR) record. The information is entered by users when the charge is posted in Charge Entry. |
| 8 | `STRING_ITEM_2` | VARCHAR |  | The value of charge generic string item 2 in the charge session (TAR) record. The information is entered by users when the charge is posted in Charge Entry. |
| 9 | `STRING_ITEM_3` | VARCHAR |  | The value of charge generic string item 3 in the charge session (TAR) record. The information is entered by users when the charge is posted in Charge Entry. |
| 10 | `NUMERIC_ITEM_1` | NUMERIC |  | The value of charge generic numeric item 1 in the charge session (TAR) record. The information is entered by users when the charge is posted in Charge Entry. |
| 11 | `NUMERIC_ITEM_2` | NUMERIC |  | The value of charge generic numeric item 2 in the charge session (TAR) record. The information is entered by users when the charge is posted in Charge Entry. |
| 12 | `NETWORKED_ITEM_1` | VARCHAR |  | The value of charge generic networked item 1 in the charge session (TAR) record. The information is entered by users when the charge is posted in Charge Entry. This item is networked to records in a masterfile defined by an administrator in the professional billing profile. |
| 13 | `NETWORKED_ITEM_2` | VARCHAR |  | The value of charge generic networked item 2 in the charge session (TAR) record. The information is entered by users when the charge is posted in Charge Entry. This item is networked to records in a masterfile defined by an administrator in the professional billing profile. |
| 14 | `BACKEND_NUMERIC_1` | NUMERIC |  | The value of charge generic backend numeric item 1 in the charge session (TAR) record. The information is entered programmatically. Contact your administrator or Epic representative to find out the meaning of the data. |
| 15 | `BACKEND_NUMERIC_2` | NUMERIC |  | The value of charge generic backend numeric item 2 in the charge session (TAR) record. The information is entered programmatically. Contact your administrator or Epic representative to find out the meaning of the data. |
| 16 | `BACKEND_NUMERIC_3` | NUMERIC |  | The value of charge generic backend numeric item 3 in the charge session (TAR) record. The information is entered programmatically. Contact your administrator or Epic representative to find out the meaning of the data. |
| 17 | `BACKEND_NUMERIC_4` | NUMERIC |  | The value of charge generic backend numeric item 4 in the charge session (TAR) record. The information is entered programmatically. Contact your administrator or Epic representative to find out the meaning of the data. |
| 18 | `BACKEND_NUMERIC_5` | NUMERIC |  | The value of charge generic backend numeric item 5 in the charge session (TAR) record. The information is entered programmatically. Contact your administrator or Epic representative to find out the meaning of the data. |
| 19 | `BACKEND_NUMERIC_6` | NUMERIC |  | The value of charge generic backend numeric item 6 in the charge session (TAR) record. The information is entered programmatically. Contact your administrator or Epic representative to find out the meaning of the data. |
| 20 | `BACKEND_NUMERIC_7` | NUMERIC |  | The value of charge generic backend numeric item 7 in the charge session (TAR) record. The information is entered programmatically. Contact your administrator or Epic representative to find out the meaning of the data. |
| 21 | `BACKEND_STRING_1` | VARCHAR |  | The value of charge generic backend string item 1 in the charge session (TAR) record. The information is entered programmatically. Contact your administrator or Epic representative to find out the meaning of the data. |
| 22 | `BACKEND_STRING_2` | VARCHAR |  | The value of charge generic backend string item 2 in the charge session (TAR) record. The information is entered programmatically. Contact your administrator or Epic representative to find out the meaning of the data. |
| 23 | `BACKEND_STRING_3` | VARCHAR |  | The value of charge generic backend string item 3 in the charge session (TAR) record. The information is entered programmatically. Contact your administrator or Epic representative to find out the meaning of the data. |
| 24 | `BACKEND_STRING_4` | VARCHAR |  | The value of charge generic backend string item 4 in the charge session (TAR) record. The information is entered programmatically. Contact your administrator or Epic representative to find out the meaning of the data. |
| 25 | `BACKEND_STRING_5` | VARCHAR |  | The value of charge generic backend string item 5 in the charge session (TAR) record. The information is entered programmatically. Contact your administrator or Epic representative to find out the meaning of the data. |
| 26 | `BACKEND_STRING_6` | VARCHAR |  | The value of charge generic backend string item 6 in the charge session (TAR) record. The information is entered programmatically. Contact your administrator or Epic representative to find out the meaning of the data. |
| 27 | `BACKEND_STRING_7` | VARCHAR |  | The value of charge generic backend string item 7 in the charge session (TAR) record. The information is entered programmatically. Contact your administrator or Epic representative to find out the meaning of the data. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

