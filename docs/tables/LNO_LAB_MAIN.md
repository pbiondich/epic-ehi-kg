# LNO_LAB_MAIN

> Primary Lab Result Report (LNO) data.

**Primary key:** `RECORD_ID`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the LNO record. |
| 2 | `LAB_REP_DATA_DATE` | DATETIME |  | The date the report data was filled into the Patient Summary Extract (LNO) record. This usually contains the report date. |
| 3 | `LAB_ID_LAB_NAME` | VARCHAR |  | The name of the lab record. |
| 4 | `DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 5 | `LAB_REPORT_TYPE_C_NAME` | VARCHAR |  | The result report type category number for the result report. |
| 6 | `REQUISITION_ID` | NUMERIC | shared | Stores the requisition record if any for which this record was created. |
| 7 | `SUBMITTER_ID` | NUMERIC |  | This is the submitter associated with the specimen on the report. |
| 8 | `SUBMITTER_ID_RECORD_NAME` | VARCHAR |  | The name of the submitter record. |
| 9 | `REQ_GRP_ID` | NUMERIC |  | This is the reference lab patient associated with the specimen on the report. |
| 10 | `CASE_ID` | NUMERIC | shared | Stores the case record for which this record was created. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

