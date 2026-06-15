# DOCS_RCVD_RSLT_COMPS

> This table stores discrete result component information received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 41  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `RESULT_COMP_KEY` | VARCHAR |  | Key to link the component with the order |
| 6 | `COMP_REFID` | VARCHAR |  | Unique Identifier for each result component. |
| 7 | `RESULT_COMP_NAME` | VARCHAR |  | Free text name for the result component |
| 8 | `RESULT_COMP_ID` | NUMERIC |  | This item stores the mapped result component in the internal system. |
| 9 | `RESULT_COMP_ID_NAME` | VARCHAR |  | The name of the component. |
| 10 | `RESULT_COMP_ABBR` | VARCHAR |  | result component abbreviation |
| 11 | `RESULT_COMP_GROUP` | VARCHAR |  | grouper for the result components |
| 12 | `RESULT_COMP_LOINC` | VARCHAR |  | LOINC code for this result component |
| 13 | `RESULT_VALUE` | VARCHAR |  | Actual value of the result |
| 14 | `RES_VAL_ST_LINE` | INTEGER |  | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 15 | `RES_VAL_END_LINE` | INTEGER |  | The end line of result text in stored in Result Impression Information. |
| 16 | `COMPONENT_COMMENT` | VARCHAR |  | The comment of a result component when less than 255 characters. |
| 17 | `COMP_CMT_ST_LINE` | INTEGER |  | The line number of result component comments greater than 254 characters |
| 18 | `COMP_CMT_END_LINE` | INTEGER |  | The line number of result component comments greater than 254 characters |
| 19 | `RESULT_UNITS` | VARCHAR |  | Units of measure for the result |
| 20 | `RESULT_FLAG_NAME` | VARCHAR |  | Free text version of the results flag |
| 21 | `RESULT_FLAG_C_NAME` | VARCHAR | org | Abnormal flag for the result |
| 22 | `RESULT_LOW_RANGE` | VARCHAR |  | Low end of the normal range for this result |
| 23 | `RESULT_HIGH_RANGE` | VARCHAR |  | High end of the normal range for this result |
| 24 | `RESULT_NORMAL` | VARCHAR |  | Normal reference range for the result |
| 25 | `RESULT_COMP_STAT_C_NAME` | VARCHAR |  | Status for the individual result component |
| 26 | `UNRECOG_VALUE_TYPE` | VARCHAR |  | One or more types of values that couldn't be parsed from CDA. |
| 27 | `LRR_ID_AND_INSTANT` | VARCHAR |  | The linked component record ID for this component, concatenated with the result instant. |
| 28 | `COMP_LOINC_AND_INST` | VARCHAR |  | The LOINC code for this component, concatenated with the result instant |
| 29 | `RSLT_COMP_STAT_ID_C_NAME` | VARCHAR |  | This item stores the mapped result component status. |
| 30 | `RSLT_COMP_LOINC_ID_LNC_LONG_NAME` | VARCHAR |  | The more readable format than the fully specified name in Logical Observation Identifiers Names and Codes (LOINC®) code. |
| 31 | `COMP_LAB_REF_IDENT` | VARCHAR |  | This item stores the lab reference ID for a specific component of a result. |
| 32 | `RSLT_VALUE_RTF_ID` | VARCHAR |  | The unique identifier for the Notes record that contains the result value in RTF format. |
| 33 | `RSLT_COMMENT_RTF_ID` | VARCHAR |  | The unique identifier for the Notes record that contains the result comment in RTF format. |
| 34 | `COMP_SIGNATURE` | VARCHAR |  | Signature of the pathologist who verified the component |
| 35 | `COMP_SIG_ST_LINE` | INTEGER |  | The line number of result component signatures greater than 200 characters |
| 36 | `COMP_SIG_END_LINE` | INTEGER |  | The end line number of result component signatures greater than 200 characters |
| 37 | `RESULT_COMP_LRR` | NUMERIC |  | The record ID of the lab component (LRR) in the constituent system. |
| 38 | `RSLT_COMP_EFF_TIME_DTTM` | DATETIME (Local) |  | This is the result time parsed from a component associated with a result. This will be used instead of the result time when populated for searching for result components for non-Epic organizations. |
| 39 | `RSLT_COMP_UA_FLG_YN` | VARCHAR |  | This represents whether a result component was explicitly considered unsuccessful by the sending organization. |
| 40 | `RSLT_COMP_BULK_STAT_C_NAME` | VARCHAR |  | The status of this data element within DINE. |
| 41 | `RSLT_COMP_BULK_INCL_DATE` | DATETIME |  | The date to compare to the change tracking window when loading flat files in bulk via DINE. If the date is within the window, but the data element is missing from the load, then the data element is invalidated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

