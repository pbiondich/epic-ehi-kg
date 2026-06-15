# RES_RPT_CMT_PTR_RM

> For a given repeat line this holds all the pointers to the table that stores the multi line comment data.

**Primary key:** `RESULT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record for this row. This column is frequently used to link to the RES_COMPONENTS table or the RES_MICRO_CULTURE table. |
| 2 | `GROUP_LINE` | INTEGER | PK | This is the repeat component line number from the RES_REPEAT_COMP table. Use the RESULT_ID to link the RES_REPEAT_COMP table to this table in addition to the GROUP_LINE. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple comments that are associated with the component/organism and the result from the RES_CMT_DATA_RM table. This column can be ignored - it is here for completeness. |
| 4 | `RPT_MLTLN_USER_CMMT` | NUMERIC |  | Stores a list of lines in OVR-52202 which store data for this line in the component related group. To link tables RES_RPT_CMT_PTR_RM to RES_CMT_DATA_RM link the following two sets of columns: - RES_RPT_CMT_PTR_RM.RESULT_ID to RES_CMT_DATA_RM.RESULT_ID, and - RES_RPT_CMT_PTR_RM.RPT_MLTLN_USER_CMMT to RES_CMT_DATA_RM.GROUP_LINE |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

