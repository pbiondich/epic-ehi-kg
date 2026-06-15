# IDENTITY_HQA_ID_HX

> This table contains the system Master Person Index (MPI) ID history for questionnaire answers. Each questionnaire answer may have multiple MPI IDs. A line number is used to identify each identification number for a questionnaire answer. A row will only exist in this table if an ID is no longer valid for a questionnaire answer record.

**Primary key:** `ANSWER_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ANSWER_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the answer record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MPI_HX_IDENTITY_ID` | VARCHAR |  | The historical identifier - if any - that resulted from the audit event. |
| 4 | `MPI_HX_INSTANT_DTTM` | DATETIME (Attached) |  | The instant at which the audit event was logged for the identifier. |
| 5 | `MPI_HX_IDENTITY_TYPE_ID` | NUMERIC |  | The ID Type (IIT) ID of the identifier. |
| 6 | `MPI_HX_IDENTITY_TYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 7 | `MPI_HX_USER_ID` | VARCHAR |  | The User (EMP) ID that triggered the audit event for the identifier. |
| 8 | `MPI_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `MPI_HX_AUDIT_CHG_TYPE_C_NAME` | VARCHAR |  | The audit event type for the update made to the identifier. |
| 10 | `MPI_HX_NEW_ID` | VARCHAR |  | The new identifier - if any - that resulted from the audit event. |
| 11 | `MPI_HX_DOTONE` | VARCHAR |  | The internal Chronicles ID of the record for which this audit event was logged. |
| 12 | `MPI_HX_ID_EFF_FROM_DATE` | DATETIME |  | The effective "from" date - if it is new or updated - for the identifier. |
| 13 | `MPI_HX_ID_EFF_TO_DATE` | DATETIME |  | The effective "to" date - if it is new or updated - for the identifier. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANSWER_ID` | [CL_QANSWER](CL_QANSWER.md) | sole_pk | high |

