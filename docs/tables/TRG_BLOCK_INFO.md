# TRG_BLOCK_INFO

> This table contains information about certain types of planned orders, including orders from treatment days in treatment plans and therapy plans, and orders from clinical pathways steps.

**Primary key:** `REGIMEN_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 23  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGIMEN_ID` | NUMERIC | PK shared | The treatment day ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The line number that corresponds to each order block in the treatment day in this row. |
| 4 | `CONTACT_DT` | DATETIME |  | The contact date in external format of the treatment day in this row. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | ID of the deployment owner for this contact. |
| 6 | `BLOCK_ID` | VARCHAR |  | The ID of an order block in the treatment day in this row. In an IntraConnect environment this column contains the community ID (CID). |
| 7 | `BLOCK_DAT` | VARCHAR |  | The contact date (DAT) of an order block in the treatment day in this row. |
| 8 | `BLOCK_INI` | VARCHAR |  | The master file (INI) of an order block in the treatment day in this row. For example, "OTP". |
| 9 | `BLOCK_DURATION` | NUMERIC |  | The duration of an order block in the treatment day in this row. |
| 10 | `BLOCK_CAT_C_NAME` | VARCHAR | org | The category of an order block in the treatment day in this row. |
| 11 | `BLOCK_WAIT_AFTER` | NUMERIC |  | The number of days to wait after an order block in the treatment day in this row. |
| 12 | `BLOCK_WAIT_FROM_C_NAME` | VARCHAR |  | The 'wait after' category of an order block in the treatment day in this row. For example, Start or End. |
| 13 | `BLOCK_MAX_LEAD` | NUMERIC |  | The max lead of an order block in the treatment day in this row. |
| 14 | `BLOCK_MAX_LAG` | NUMERIC |  | The max lag of an order block in the treatment day in this row. |
| 15 | `BLOCK_SOURCE` | VARCHAR |  | The source ID of an order block in the treatment day in this row. |
| 16 | `BLOCK_OTP_ID` | NUMERIC |  | The unique ID of the order block (patient order template) in the treatment day in this record. |
| 17 | `CHILD_DISPLAY_NAME` | VARCHAR |  | The display name of an order block in the treatment day in this record. |
| 18 | `CHILD_SSC_ID` | NUMERIC |  | The unique ID of a non-order block in the treatment day in this record. |
| 19 | `CHILD_RECOMMEND_YN` | VARCHAR |  | The flag indicating if the order item is recommended with an override reason. |
| 20 | `CHILD_REC_OVR_RSN_C_NAME` | VARCHAR | org | The reason for deselecting the recommended item |
| 21 | `CHILD_RECOM_OVR_CMT` | VARCHAR |  | The comments for deselecting the recommended item |
| 22 | `BLOCK_SRC_DAY_UID` | VARCHAR |  | Stores the unique ID of the day from which it was created. |
| 23 | `ORDER_RANK` | INTEGER |  | Stores the position of this order in the treatment day from the source protocol. If this order was added manually to the treatment plan after it was created, then this item will be empty. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

