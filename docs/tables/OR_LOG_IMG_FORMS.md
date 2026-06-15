# OR_LOG_IMG_FORMS

> This table contains forms which correspond to log images.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the log record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FORM_ID` | VARCHAR | FK→ | The unique ID of the for record. |
| 4 | `FORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 5 | `FORM_LIST_ID` | INTEGER |  | Identifier for the form in the log. |
| 6 | `FORM_DAT` | NUMERIC |  | The contact of the form. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FORM_ID` | [CL_QFORM1](CL_QFORM1.md) | sole_pk | high |

