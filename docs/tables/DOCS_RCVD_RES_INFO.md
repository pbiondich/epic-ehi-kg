# DOCS_RCVD_RES_INFO

> The DOCS_RCVD_RES_INFO table contains information about compiled received results such as result time, procedure, status and specimen type.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique ID of received documents. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RESULT_INST_CMP_DTTM` | DATETIME (Local) |  | The instant when the result was collected or resulted. |
| 4 | `RES_PROC_NAME_CMP` | VARCHAR |  | The free text name of the procedure. |
| 5 | `RES_PROC_CMP_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 6 | `RESULT_ENC_ID_CMP` | VARCHAR |  | The unique ID of the encounter during which the order took place. |
| 7 | `RESULT_KEY_CMP` | VARCHAR |  | The unique key that links other result information to this order. |
| 8 | `RES_STATUS_CMP_C_NAME` | VARCHAR |  | The result status category ID for the received information. |
| 9 | `RES_ABN_CMP` | VARCHAR |  | The value that indicates whether this result was flagged as abnormal or normal. |
| 10 | `RSLT_SPECIMEN` | VARCHAR |  | Information about the specimen source/type as sent by the outside organization. |
| 11 | `RSLT_UNSUCC_FLG_COMP_C_NAME` | VARCHAR |  | Indicates whether a result was deemed an unsuccessful attempt |
| 12 | `RSLT_UNSUCC_INST_COMP_UTC_DTTM` | DATETIME (UTC) |  | The instant the result unsuccessful flag was set |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

