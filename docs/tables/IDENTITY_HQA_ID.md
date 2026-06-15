# IDENTITY_HQA_ID

> THE IDENTITY_HQA_ID table contains the system Master Person Index (MPI) ID numbers for questionnaire answers. Each questionnaire answer may have mutliple MPI ID's. A line number is used to identify each identification number for a questionnaire answer.

**Primary key:** `ANSWER_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ANSWER_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the answer record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MPI_ID_TYPE_ID` | NUMERIC |  | The ID Type (IIT) ID of the questionnaire answer (HQA) record. |
| 4 | `MPI_ID_TYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 5 | `MPI_ID` | VARCHAR |  | Identity ID assigned to the questionnaire answer (HQA) record. |
| 6 | `MPI_FROM_DATE` | DATETIME |  | The effective "from" date for the questionnaire answer Identity ID. |
| 7 | `MPI_TO_DATE` | DATETIME |  | The effective "to" date for questionnaire answer Identity ID. |
| 8 | `MPI_RET_CHK_LPP_ID` | NUMERIC |  | The retrieval check extension. |
| 9 | `MPI_RET_CHK_LPP_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |
| 10 | `MPI_RET_CHK_RULE_ID` | VARCHAR |  | The retrieval check rule. |
| 11 | `MPI_RET_CHK_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANSWER_ID` | [CL_QANSWER](CL_QANSWER.md) | sole_pk | high |

