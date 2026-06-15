# FIN_ASST_CASE_APPL_DOC

> This table contains information about documents applicable for each patient in a financial assistance case record.

**Primary key:** `FIN_ASST_CASE_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_CASE_ID` | NUMERIC | PK FK→ | The unique identifier for the financial assistance case record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated patient in the financial assistance case record. Together with FIN_ASST_CASE_ID, this forms the foreign key to the FIN_ASST_CASE_PATIENT table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple documents associated with the financial assistance case record and a specific patient from the FIN_ASST_CASE_PATIENT table. |
| 4 | `APPLICABLE_DOC_INFO_ID` | VARCHAR |  | The unique identifier of the document applicable to a patient in the financial assistance case record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_CASE_ID` | [FIN_ASST_CASE](FIN_ASST_CASE.md) | sole_pk | high |

