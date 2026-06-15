# MTP_AUTO_EVAL_LAB_RESULTS

> Information for lab results obtained by automated evaluations for medication therapy problems.

**Primary key:** `PROBLEM_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the med therapy problem record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RESULT_COMPONENT_ID` | NUMERIC |  | The lab component identified by the automated evaluation for the medication therapy problem. |
| 4 | `RESULT_COMPONENT_ID_NAME` | VARCHAR |  | The name of the component. |
| 5 | `FILED_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The instant that the lab result was filed. |
| 6 | `ORDER_ID` | NUMERIC | shared | The order for the lab result identified by the automated evaluation for the medication therapy problem. |
| 7 | `RESULT_COMPONENT_LNC_ID_LNC_LONG_NAME` | VARCHAR |  | The more readable format than the fully specified name in Logical Observation Identifiers Names and Codes (LOINC®) code. |
| 8 | `AUTO_EVAL_ORDER_DAT` | NUMERIC |  | The order contact on which the lab result was found during the medication therapy problem automated evaluation. |
| 9 | `AUTO_EVAL_ORDER_LINE` | INTEGER |  | The order line on which the lab result was found during the medication therapy problem automated evaluation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |

