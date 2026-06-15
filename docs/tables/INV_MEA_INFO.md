# INV_MEA_INFO

> This table contains test result information (e.g. hematocrit readings, hemoglobin readings etc.) from the invoice record.

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The invoice record ID. |
| 2 | `LINE` | INTEGER | PK | This column contains the line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MEA_TEST_C_NAME` | VARCHAR | org | This column contains the test result qualifier. |
| 4 | `MEA_RESULT` | NUMERIC |  | This column contains the test result value. |
| 5 | `MEA_IDENTIFIER_C_NAME` | VARCHAR | org | This column contains the test result identifier. |
| 6 | `MEA_LINE_INDEX` | NUMERIC |  | This column contains the test result service line index. This column contains a line number that corresponds to the claim line to which the test result is related. |
| 7 | `MEA_TEST_DATE` | DATETIME |  | This column contains the test performed date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

