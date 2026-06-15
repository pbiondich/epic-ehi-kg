# FIN_ASST_TRKR_RST_ACCL_HX

> This table contains a history of edits made to the list of account class restrictions placed on a financial assistance tracker record to limit the scope of tracker's approval.

**Primary key:** `FIN_ASST_TRACKER_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_TRACKER_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the financial assistance program tracker record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the accout classes approval is restricted to at the time of this update in the financial assistance tracker record. Together with FIN_ASST_TRACKER_ID column in this table, this forms the foreign key to the FIN_ASST_TRKR_UPDATE_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple account classes approval is restricted to with the financial assistance tracker record and the update from the FIN_ASST_TRKR_UPDATE_HX table. |
| 4 | `UPDATE_ADT_PAT_CLASS_C_NAME` | VARCHAR | org | The account class category ID of one of the account classes the financial assistance tracker record's approval is restricted to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_TRACKER_ID` | [FIN_ASST_TRACKER](FIN_ASST_TRACKER.md) | name_stem | high |

