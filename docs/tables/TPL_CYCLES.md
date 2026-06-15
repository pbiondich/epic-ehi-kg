# TPL_CYCLES

> The cycle information for the treatment plan.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The treatment plan ID. |
| 2 | `LINE` | INTEGER | PK | The line number that corresponds to each cycle in the treatment plan in this row. |
| 3 | `CYCLE_ID` | VARCHAR | FK→ | The treatment plan level ID for the cycle in this row. |
| 4 | `CYCLE_NAME` | VARCHAR |  | The cycle name of the cycle in this row. |
| 5 | `CYCLE_STATUS_C_NAME` | VARCHAR |  | The cycle status of the cycle in this row. For example, Planned, Started, Completed, Deleted, or Snapshot. |
| 6 | `CYCLE_START_DATE` | DATETIME |  | The start date of the cycle in this row, in calendar format. |
| 7 | `CYCLE_WAIT_AFTER` | NUMERIC |  | The number of days to wait after the cycle in this row. |
| 8 | `CYCLE_MAX_LEAD` | NUMERIC |  | The max lead for the cycle in this row. |
| 9 | `CYCLE_MAX_LAG` | NUMERIC |  | The max lag for the cycle in this row. |
| 10 | `ANCHOR_DAY` | NUMERIC |  | The treatment plan level ID of the anchor day for the cycle in this row. |
| 11 | `CYCLE_CREATED_BY_ID` | VARCHAR |  | The user ID of the person who created the cycle in this row. |
| 12 | `CYCLE_CREATED_BY_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `CYCLE_CREATED_ON_TM` | DATETIME (Local) |  | The date and time of creation in external format for the cycle in this row. |
| 14 | `CYCLE_COMMENT` | VARCHAR |  | The cycle creation comment for the cycle in this row. |
| 15 | `CYCLE_NUM` | INTEGER |  | The cycle number of this cycle for this treatment plan. |
| 16 | `CYC_STAT_CHG_USR_ID` | VARCHAR |  | Stores the user who changed the cycle status. |
| 17 | `CYC_STAT_CHG_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 18 | `CYC_STAT_CHG_DTTM` | DATETIME (Local) |  | Stores the instant at which the cycle status changed. |
| 19 | `CYC_STAT_CHG_COMM` | VARCHAR |  | Stores comment entered by user when changing the status. |
| 20 | `CYC_SOURCE_UID` | VARCHAR |  | Stores the unique ID of the cycle from which it was created. |
| 21 | `PRL_CYCLE_SRC_ID` | VARCHAR |  | If this treatment plan cycle was created from a protocol, this item will be set to the Cycle ID (I PRL 200) that created this treatment plan cycle. This column will match the CL_PRL_CYCLES__PRL_CYCLE_ID column. |
| 22 | `CONVERSION_CYC_TRGT` | INTEGER |  | If this cycle was replaced by another cycle when conversion is accepted or discarded, this will be the line of the cycle that replaced it (SI TPL 1000). |
| 23 | `CYCLE_PATTERN_SOURCE_LINE` | INTEGER |  | For this cycle, if it was created from a pattern cycle, this item will store the source line in SI TPL 12000 it was created from. |
| 24 | `CYCLE_CREATION_METHOD_C_NAME` | VARCHAR |  | If this cycle was created from a repeating cycle, this column specifies whether it was created manually or automatically. This item will be blank if the cycle was not created from a repeating cycle, or if it was created by copying and pasting a repeating cycle. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CYCLE_ID` | [INFERTILITY_CYCLE](INFERTILITY_CYCLE.md) | sole_pk | high |

