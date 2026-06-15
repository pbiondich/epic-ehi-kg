# V_EHI_CVG_COVERAGE_HIST_MEM

> Filter view for loading coverage history by member as EHI.

**Primary key:** `COVERAGE_ID`, `LINE`, `INFO_LINE`  
**Columns:** 18  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique ID assigned to the coverage record. This ID may be encrypted if you have elected to use enterprise reporting’s encryption utility. |
| 2 | `LINE` | INTEGER | PK | The line number used to identify each row of history information for a coverage record. |
| 3 | `CHANGE_DATE` | DATETIME |  | The date on which each change was added to the coverage record. |
| 4 | `ACTION_C_NAME` | VARCHAR |  | The category value associated with the change made to the coverage record (i.e. Create, Add Member, Change Covered Status, etc.) |
| 5 | `EDIT_INFO` | VARCHAR |  | The original information associated with the change. |
| 6 | `EDIT_PAT_ID` | VARCHAR | FK→ | The member ID for whom the change is done. |
| 7 | `EFF_DT_CHNG_RSN_C_NAME` | VARCHAR | org | The effective date change reason in the Coverage History. |
| 8 | `MC_EDIT_HX_TIME` | DATETIME (Local) |  | Coverage history time of change. |
| 9 | `INFO_RCVD_DT` | DATETIME |  | The information received date associated with the change. |
| 10 | `INFO_LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 11 | `ITEM` | INTEGER |  | The item associated with the old and new values of this line. |
| 12 | `IS_KEY_ITEM_YN` | VARCHAR |  | Indicates whether the item on this line is a key item for the action associated with this line. The set values (old and new separately) of key items in the same group for the same action cannot be duplicated across other groups of that action. 'Y' indicates that the item is a key item. 'N' or NULL indicates that the item is not a key item. |
| 13 | `OLD_VALUE` | VARCHAR |  | The old value of the item on this line. |
| 14 | `NEW_VALUE` | VARCHAR |  | The new value of the item on this line. |
| 15 | `OLD_CID` | VARCHAR |  | If the item on this line is a category item or a networked item, the CID associated with the old value of the item on this line. |
| 16 | `NEW_CID` | VARCHAR |  | If the item on this line is a category item or a networked item, the CID associated with the new value of the item on this line. |
| 17 | `GROUP_NUM` | INTEGER |  | A number that groups a set of items together in an action. If the group number is 0, it means the item and its values apply to every group in the action. |
| 18 | `CHANGE_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant that the change happened. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `EDIT_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

