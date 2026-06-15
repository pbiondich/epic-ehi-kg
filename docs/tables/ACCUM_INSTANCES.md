# ACCUM_INSTANCES

> This table contains general information about accumulation instances.

**Primary key:** `ACCUMULATION_ID`, `LINE`  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCUMULATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the accumulation record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACCUM_GROUP_ID` | NUMERIC |  | The accumulation group associated with the accumulation instance. |
| 4 | `ACCUM_PREV_ACC_ID` | NUMERIC |  | The ID of the previous accumulation applied to the associated accumulation group. |
| 5 | `ACCUM_PREV_ACC_LN` | INTEGER |  | The line in related group 90 from the accumulation corresponding to the previous accumulation instance. |
| 6 | `ACCUM_APPLIED_AMT` | NUMERIC |  | The amount applied to the associated accumulation group. |
| 7 | `ACCUM_RUNNING_TOTAL` | NUMERIC |  | The running total for the associated ACG after this accumulation instance was added. |
| 8 | `ACCUMULATION_INSTANT_DTTM` | DATETIME (UTC) |  | The instant this accumulation happened. |
| 9 | `TARGET_AMOUNT` | NUMERIC |  | The amount that we attempt to accumulate towards the associated accumulation group (ACG). |
| 10 | `REVERSED_LINE` | INTEGER |  | The line in this ACC's related group 90 which is reversed by this line. |
| 11 | `SEQUENCE_NUMBER` | INTEGER |  | The position in the sequence of accumulation instances this line represents for the associated accumulation group. |
| 12 | `ACCUM_LIMIT_AMT` | NUMERIC |  | The limit amount for the associated ACG when this accumulation instance was added. |
| 13 | `ADJUD_SEQ_NUM` | INTEGER |  | The number of times the claim has been priced by the adjudicator when this accumulation instance was added. |
| 14 | `VISIT_ACCUM_GRP_ID` | NUMERIC |  | The visit (represented by a Benefits Visit ACG, separate from the one accumulated to on this line) that was counted towards the Benefit Limit Mechanism ACG on this line. |
| 15 | `CARRY_FLAG_C_NAME` | VARCHAR |  | Stores a category value representing the type of carryover workflow that resulted in the accumulation. |
| 16 | `CARRY_FROM_COVERAGE_ID` | NUMERIC |  | Stores the source coverage this accumulation was carried from if it is a result of coverage to coverage carryover. |
| 17 | `ACCUM_SERVICE_DATE` | DATETIME |  | The service date at the time the accumulation line was generated (or, if it's a reversal line, the time the original accumulation line was generated). |
| 18 | `WAS_LIMIT_CHECKED_YN` | VARCHAR |  | Says whether the limit was checked during adjudication when we originally calculated the accumulation amount |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

