# IMAGING_CDS_ORDER_TEMPLT

> This table contains the appropriateness score and associated information for an imaging procedure if using third party decision support software in conjunction with Epic.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient order template record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DECISION_SUPPORT_ID` | VARCHAR |  | Unique ID for the decision support session. |
| 4 | `DS_SCORE_C_NAME` | VARCHAR | org | Appropriateness score calculated by a clinical decision support system |
| 5 | `DS_SOURCE_C_NAME` | VARCHAR |  | Stores the activity which saved the decision support score for an imaging order. |
| 6 | `DS_CDSM_VENDOR_C_NAME` | VARCHAR | org | Stores the decision support vendor that was consulted as a category value. |
| 7 | `DS_ADHERENCE_IND_C_NAME` | VARCHAR |  | Stores an adherence indication value (Y/N/NCA) from the Clinical Decision Support Mechanism (CDSM) |
| 8 | `DS_CONSULT_UTC_DTTM` | DATETIME (UTC) |  | Stores an instant in UTC of when the Clinical Decision Support Mechanism (CDSM) was consulted |
| 9 | `DS_COMMENT` | VARCHAR |  | Stores comments by the ordering provider regarding AUC information |
| 10 | `DS_EXCEPTION_C_NAME` | VARCHAR |  | Stores an exception reason for missing consulting the Clinical Decision Support Mechanism (CDSM) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

