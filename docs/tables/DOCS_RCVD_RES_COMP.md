# DOCS_RCVD_RES_COMP

> The DOCS_RCVD_RES_COMP table contains information about compiled results components.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 22  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique ID of received documents. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RES_CMP_KEY_CMP` | VARCHAR |  | The key which links the component with the order. |
| 4 | `RES_COMP_NAME_CMP` | VARCHAR |  | The free text name of the result component. |
| 5 | `RES_CMP_CMP_ID` | NUMERIC |  | The internal ID of the component to which this result was mapped. This column links to the CLARITY_LRR table. |
| 6 | `RES_CMP_CMP_ID_NAME` | VARCHAR |  | The name of the component. |
| 7 | `RES_COMP_ABBR_COMP` | VARCHAR |  | The abbreviation for the result component. |
| 8 | `RES_COMP_GRP_COMP` | VARCHAR |  | The list of component groups that the component belongs to. |
| 9 | `RES_COMP_LOINC_CMP` | VARCHAR |  | The LOINC code identifier for the component. |
| 10 | `RES_VAL_COMP` | VARCHAR |  | The value for this result (populated if a single-line value). |
| 11 | `RES_VAL_ST_LINE_CMP` | INTEGER |  | The start line for the result component's value (populated if a multi-line value). The line maps to a line in the DOCS_RCVD_RES_TEXT table. |
| 12 | `RES_VAL_END_LN_CMP` | INTEGER |  | The end line for the result component's value (populated if a multi-line value). The line maps to a line in the DOCS_RCVD_RES_TEXT table. |
| 13 | `RES_COMMENT_COMP` | VARCHAR |  | The comment for the result value (populated if a single-line value). |
| 14 | `RES_CMT_ST_LINE_CMP` | INTEGER |  | The start line for the result component's comment (populated if a multi-line value). The line maps to a line in the DOCS_RCVD_RES_TEXT table. |
| 15 | `RES_CMT_END_LN_CMP` | INTEGER |  | The end line for the result component's comment (populated if a multi-line value). The line maps to a line in the DOCS_RCVD_RES_TEXT table. |
| 16 | `RES_UNIT_COMPILED` | VARCHAR |  | The unit of measurement for the result. |
| 17 | `RES_FLAG_NAME_CMP` | VARCHAR |  | The free text version of the result flag. |
| 18 | `RES_FLAG_COMP_C_NAME` | VARCHAR | org | The result component flag category ID for the received results. |
| 19 | `RES_LOW_RNG_CMP` | VARCHAR |  | The low end of the normal range for the result. |
| 20 | `RES_HIGH_RANGE_CMP` | VARCHAR |  | The high end of the normal range for the result. |
| 21 | `RES_NORMAL_CMP` | VARCHAR |  | The normal range for the result. |
| 22 | `RES_COMP_STAT_CMP_C_NAME` | VARCHAR |  | The result component status category ID for the received results. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

