# CL_QANSWER_VERIFY

> The CL_QANSWER_VERIFY table contains information about verifications for questionnaire answers.

**Primary key:** `ANSWER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ANSWER_ID` | VARCHAR | PK FK→ | The unique ID of the record used to store the answers to a questionnaire. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `QF_VERIFY_HVR_ID` | NUMERIC |  | Stores HVR records of verifications on these answers |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANSWER_ID` | [CL_QANSWER](CL_QANSWER.md) | sole_pk | high |

