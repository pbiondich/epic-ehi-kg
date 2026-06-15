# FIN_ASST_CASE_LNKD_TRKR

> This table contains information on how financial assistance program trackers are linked to each other in a financial assistance case.

**Primary key:** `FIN_ASST_CASE_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_CASE_ID` | NUMERIC | PK FK→ | The unique identifier for the financial assistance case record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the group of the linked financial assistance trackers in the financial assistance case record. Together with FIN_ASST_CASE_ID, this forms the foreign key to the FIN_ASST_CASE_ASSOC_TRKR table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple financial assistance trackers associated with the financial assistance case from the FIN_ASST_CASE_ASSOC_TRKR table. |
| 4 | `LINKED_FIN_ASST_TRACKER_ID` | NUMERIC |  | The unique ID of the financial assistance tracker that is part of a linked group. The financial assistance trackers in a linked group are edited as if they are one by the financial counselor. Updating one tracker will mean updating all the trackers in the linked group. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_CASE_ID` | [FIN_ASST_CASE](FIN_ASST_CASE.md) | sole_pk | high |

