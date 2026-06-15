# RES_NLP_STATUS

> Stores information related to the verification status of NLP generated findings and recommendations.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NLP_MODEL_TYPE_C_NAME` | VARCHAR |  | Stores NLP Models that have run for this record. |
| 4 | `NLP_VERIFYING_USER_ID` | VARCHAR |  | The user that verified the NLP generated results. |
| 5 | `NLP_VERIFYING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `RIS_NLP_STATUS_C_NAME` | VARCHAR |  | The verification status of an NLP Model. |
| 7 | `NLP_VERIFIED_DTTM` | DATETIME (UTC) |  | The UTC instant NLP results are verified. |
| 8 | `NLP_MODIFY_TYPE_C_NAME` | VARCHAR |  | The type of modification needed to correct NLP results. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

