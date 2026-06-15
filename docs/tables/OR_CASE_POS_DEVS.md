# OR_CASE_POS_DEVS

> The OR_CASE_POS_DEVS table contains the positioning devices information for the current case.

**Primary key:** `OR_CASE_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_CASE_ID` | VARCHAR | PK FK→ | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `POS_DEV_TYPE_C_NAME` | VARCHAR | org | The positioning device type category number for the case record. |
| 4 | `POS_DEV_REQ_YN_NAME` | VARCHAR |  | Indicates whether a positioning device will be required for the case. Y indicates that the device will be required for the case. N indicates that the device will not be required. Null indicates that there is no value configured for the case. |
| 5 | `POS_DEV_START_TM` | INTEGER |  | The time when the positioning device was started for the case. |
| 6 | `POS_DEV_END_TM` | INTEGER |  | The time when the positioning device was ended for the case. |
| 7 | `POS_DEV_PANEL_NUM` | VARCHAR |  | The panel numbers of the case in which the positioning device is used. This is a caret-delimited string of panel numbers. |
| 8 | `POS_DEV_DEFAULT_YN_NAME` | VARCHAR |  | Indicates whether a positioning device will default from the case. Y indicates that the device will default from the case. N indicates that the device will not default from the case. Null indicates that there is no value configured for the case. |
| 9 | `POS_DEV_BODYPART_C_NAME` | VARCHAR |  | The body part type category number for the case record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_CASE_ID` | [OR_CASE](OR_CASE.md) | name_stem | high |

