# RES_VAL_DATA_RM

> Stores data for multi-line value item. For a given line data may be spread across multiple lines.

**Primary key:** `RESULT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record for this row. This column is frequently used to link to the RES_COMPONENTS table through the RES_VAL_PTR_RM table. For component repeats, link from RES_REPEAT_COMP through the RES_RPT_VAL_PTR_RM table. |
| 2 | `GROUP_LINE` | INTEGER | PK | Stores a link from the RES_VAL_PTR_RM.CMP_MULTILINE_VALUE column. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values that are associated with the result and the component/organism from the RES_VAL_PTR_RM or RES_RPT_VAL_PTR_RM table. This column can be ignored - it is here for completeness. |
| 4 | `MULT_LN_VAL_STORAGE` | VARCHAR |  | The value entered for a given component. Each component can list multiple lines in Component Multiline Value (OVR-51201) (RES_VAL_PTR_RM.CMP_MULTILINE_VALUE) or Repeat Component Multiline Value (OVR-53201) (RES_RPT_VAL_PTR_RM.RPT_MULTILINE_VALUE), which are the lines of this item. If the value is a category number, this column contains the category title, not the category number, at the time of extract. If the category title is changed after the extract, this data could get out of sync. Note that the category number is also extracted to RES_VAL_DATA_RM.MULT_LN_VAL_STG_RAW, so you could look up the category title based on the category number from the corresponding category ZC table. To find out which category table to use, check the columns LAB_CAT_INI and LAB_CAT_ITEM in table CLARITY_COMPONENT for the component associated with this row. |
| 5 | `MULT_LN_VAL_STG_RAW` | VARCHAR |  | Stores the values for a given component. For a category value this would be the identifier. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

