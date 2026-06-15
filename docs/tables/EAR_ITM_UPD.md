# EAR_ITM_UPD

> This table contains guarantor item update information for a particular guarantor account item's last update. Columns included are the guarantor item to which the update information relates, the user that last updated this item, and the instant that the last update occurred. Note that the actual guarantor account item value is not included in this table: only details of the last update to the item are included.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the guarantor account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UPD_ITM_NUM` | INTEGER |  | This item contains the guarantor item number to which the update information for User (I EAR 2032) and Instant (I EAR 2033) relates. |
| 4 | `UPD_USER_ID` | VARCHAR |  | This item contains the user (EMP) ID that entered the last update for the guarantor item number (I EAR 2031). |
| 5 | `UPD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `UPD_INSTANT_DTTM` | DATETIME (UTC) |  | This item contains the instant in UTC time that the last update was made to the guarantor item number (I EAR 2031). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

