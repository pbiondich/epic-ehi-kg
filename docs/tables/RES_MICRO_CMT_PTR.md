# RES_MICRO_CMT_PTR

> This table extracts a list of lines which hold multiline comments for the isolate.

**Primary key:** `RESULT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record for this row. This column is frequently used to link to the RES_MICRO_CULTURE table. |
| 2 | `GROUP_LINE` | INTEGER | PK | This is the organism line number from the RES_MICRO_CULTURE table. Use the RESULT_ID to link the RES_MICRO_CULTURE table to this table in addition to the GROUP_LINE. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this row. |
| 4 | `CUL_MLTLN_USER_CMMT` | INTEGER |  | Stores the multiline comment for this organism isolate. A single isolate can have multiple comment lines associated with it. To link tables RES_MICRO_CMT_PTR to RES_CMT_DATA_RM link the following two sets of columns: RES_MICRO_CMT_PTR.RESULT_ID to RES_CMT_DATA_RM.RESULT_ID, and RES_MICRO_CMT_PTR.CUL_MLTLN_USER_CMMT to RES_CMT_DATA_RM.GROUP_LINE |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

