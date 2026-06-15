# RES_CMT_DATA_RM

> Stores data for multi line comment item. For a given line data may be spread across multiple lines.

**Primary key:** `RESULT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record for this row. This column is frequently used to link to the RES_COMPONENTS table or the RES_MICRO_CULTURE table through the RES_CMT_PTR_RM table. For component repeats, link from RES_REPEAT_COMP through the RES_RPT_CMT_PTR_RM table. |
| 2 | `GROUP_LINE` | INTEGER | PK | This contains a link to the RES_CMT_PTR_RM.CMP_MLTLN_USER_CMMT clarity column. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values that are associated with the result and the component/organism from the RES_CMT_PTR_RM or RES_RPT_CMT_PTR_RM table. This column can be ignored - it is here for completeness. |
| 4 | `MULTLINE_UC_STG_RAW` | VARCHAR |  | Stores the user comments for a given component. For a category value this would be the ID. Each component can list multiple lines in OVR-51202 (Component Multiline User Comment Pointer) or OVR-53202 (Repeat Component Multiline User Comment Pointer) which are the lines of this item. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

