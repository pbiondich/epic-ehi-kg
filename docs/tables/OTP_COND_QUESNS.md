# OTP_COND_QUESNS

> This table contains the inpatient condition questions (if configured) for an order template

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier of the order template record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COND_QUESN_ID_QUEST_NAME` | VARCHAR |  | The name of the question record. |
| 4 | `COND_QUESN_DAT` | NUMERIC |  | The question date of the question record that identifies the condition question for an inpatient order. |
| 5 | `COND_QUESN_RESP` | VARCHAR |  | The response to a condition question on an inpatient order. |
| 6 | `COND_QUESN_SEL_YN` | VARCHAR |  | This item indicates whether the related condition question is selected ("checked") or unselected ("unchecked") for an inpatient conditional order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

