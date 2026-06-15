# RES_REPEAT_COMP_2

> This table is used to extract information on component-level repeats.

**Overflow of:** [RES_REPEAT_COMP](RES_REPEAT_COMP.md)  
**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REPEAT_INSTRVER` | VARCHAR |  | The verification flag received from the middle tier for the component repeat. |
| 4 | `REPEAT_EQUATION` | VARCHAR |  | A string representation of the equation used to find the value for calculated component repeats. |
| 5 | `REPEAT_COMPON_TAG_LN` | INTEGER |  | Line number for the tested against group relevant to this row, indicating that all component lines pointing to the same line should be grouped together logically. |
| 6 | `RPT_CMP_ADD_USER_ID` | VARCHAR |  | The user who originally added the component |
| 7 | `RPT_CMP_ADD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `RPT_ADD_DTTM` | DATETIME (Attached) |  | Stores the local instant of when the component was originally added to the test. |
| 9 | `RPT_ADD_UTC_DTTM` | DATETIME (UTC) |  | Stores the UTC instant of when the component was originally added to the test. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

