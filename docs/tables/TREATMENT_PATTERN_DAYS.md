# TREATMENT_PATTERN_DAYS

> Treatment day patterns in a treatment plan.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PATTERN_DAY_TRG_CSN_ID` | NUMERIC |  | The unique contact serial number of the TRG that this treatment day uses. |
| 4 | `PATTERN_DAY_SORT_VALUE` | INTEGER |  | Stores the Id to identify a day in a pattern cycle. Note that multiple days can have the same Id if they are part of different pattern cycles. |
| 5 | `PATTERN_DAY_CYCLE_LINE` | INTEGER |  | The cycle pattern that this day is part of. Stored as a line in SI TPL 12000. |
| 6 | `PATTERN_DAY_DATE_IN_CYCLE` | INTEGER |  | The day in the cycle that this treatment day falls on. Will be 0 if the day falls on the cycle start date, 1 if it is the second day of the cycle, etc. |
| 7 | `PATTERN_DAY_STATUS_C_NAME` | VARCHAR |  | The treatment day status category Id for the pattern treatment day. |
| 8 | `PATTERN_DAY_NAME` | VARCHAR |  | Tha name for this pattern day. This will be set as the name of the treatment day that will be created from this pattern day. |
| 9 | `PATTERN_DAY_TYPE_C_NAME` | VARCHAR |  | The inpatient or outpatient category Id for the pattern treatment day. |
| 10 | `PATTERN_DAY_NUM` | INTEGER |  | That day number in the cycle of a pattern day. |
| 11 | `PATTERN_DAY_LENGTH` | INTEGER |  | The length of a treatment day. Always 1 for outpatient days but can be 1 or more for inpatient days. |
| 12 | `PATTERN_DAY_SRC_TYPE_C_NAME` | VARCHAR |  | The type of day this pattern day was created from. |
| 13 | `PATTERN_DAY_SOURCE_LINE` | INTEGER |  | The line in the source where this day was created from. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

