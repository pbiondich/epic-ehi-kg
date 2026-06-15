# PAT_TEMP_DTREES

> This table houses information regarding the decision trees that are currently not fully completed by the patient.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_TMP_DTREE_ID` | VARCHAR |  | Stores decision trees that haven't been completed by the patient yet. |
| 4 | `PAT_TMP_DTREE_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 5 | `PAT_TMP_DTREE_ANSWER_ID` | VARCHAR |  | Stores the answer record for the corresponding in-progress decision tree. |
| 6 | `PAT_TMP_DTREE_STATUS_C_NAME` | VARCHAR |  | Stores the status of the corresponding in-progress decision tree. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

