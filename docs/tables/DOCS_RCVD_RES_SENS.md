# DOCS_RCVD_RES_SENS

> The DOCS_RCVD_RES_SENS table contains information about compiled results susceptibility.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 23  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RES_SENS_KEY_CMP` | VARCHAR |  | The key which links the result susceptibility with the order. |
| 4 | `RES_SENS_ORG_N_CMP` | VARCHAR |  | The free text name of the susceptibility organism. |
| 5 | `RES_SENS_ORG_CMP_ID` | NUMERIC |  | The internal ID of the organism to which this susceptibility was mapped. |
| 6 | `RES_SENS_ORG_CMP_ID_NAME` | VARCHAR |  | The name of the organism. |
| 7 | `RES_SENS_ORG_SUBID` | VARCHAR |  | A unique ID to differentiate multiple tests on the same organism. |
| 8 | `RES_SENS_ORG_CMT` | VARCHAR |  | The comment for a result organism (populated if a single-line value). |
| 9 | `RES_SENS_ORG_CMT_SL` | INTEGER |  | The start line for the result organism's comment (populated if a multi-line value). The line maps to a line in the DOCS_RCVD_RES_TEXT table. |
| 10 | `RES_SENS_ORG_CMT_EL` | INTEGER |  | The end line for the result organism's comment (populated if a multi-line value). The line maps to a line in the DOCS_RCVD_RES_TEXT table. |
| 11 | `RES_SENS_ANT_NM_CMP` | VARCHAR |  | The free text name of the antibiotic used. |
| 12 | `RES_SENS_ANTIB_ID_C_NAME` | VARCHAR | org | The internal category of the antibiotic to which this susceptibility was mapped. |
| 13 | `RES_SENS_SUS_NM_CMP` | VARCHAR |  | The free text name of the susceptibility result. |
| 14 | `RES_SENS_SUSC_ID_C_NAME` | VARCHAR | org | The internal category of the antibiotic to which this susceptibility was mapped. |
| 15 | `RES_SENS_VALUE_SL` | INTEGER |  | The start line for the result susceptibility value (populated if a multi-line value). The line maps to a line in the DOCS_RCVD_RES_TEXT table. |
| 16 | `RES_SENS_VALUE_EL` | INTEGER |  | The end line for the result susceptibility value (populated if a multi-line value). The line maps to a line in the DOCS_RCVD_RES_TEXT table. |
| 17 | `RES_SENS_CMT_CMP` | VARCHAR |  | The free text comment for this susceptibility. |
| 18 | `RES_SENS_COMMENT_SL` | INTEGER |  | The start line for the result susceptibility comment (populated if a multi-line value). The line maps to a line in the DOCS_RCVD_RES_TEXT table. |
| 19 | `RES_SENS_COMMENT_EL` | INTEGER |  | The end line for the result susceptibility comment (populated if a multi-line value). The line maps to a line in the DOCS_RCVD_RES_TEXT table. |
| 20 | `RES_SENS_MTH_NM_CMP` | VARCHAR |  | The free text name of the method used to assess the susceptibility. |
| 21 | `RES_SEN_MTHD_CMP_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 22 | `RES_SENS_SUP_FLAG_YN` | VARCHAR |  | Whether the antibiotic result is hidden from end users when viewed within the patient's chart. Its intended use is to suppress results for broad spectrum or second line agents when the lab system believes there is a viable first line treatment reported. |
| 23 | `RES_SENS_ANLYS_UTC_DTTM` | DATETIME (UTC) |  | Timestamp to track per micro result component when it was analyzed in lab. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

