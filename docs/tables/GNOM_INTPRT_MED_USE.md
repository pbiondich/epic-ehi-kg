# GNOM_INTPRT_MED_USE

> Medication usage recommendations as part of an interpretation.

**Primary key:** `GNOM_INTPRT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GNOM_INTPRT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the interpretation record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `PGX_MED_CODESET_C_NAME` | VARCHAR |  | Stores the code set used for identifying a coded medication assessed in a pharmacogenomic test. |
| 5 | `PGX_MED_CODE` | VARCHAR |  | Stores the coded identifier for a medication assessed in a pharmacogenomic test. |
| 6 | `ASSOC_MED_NAME` | VARCHAR |  | Stores the name of a medication assessed in a pharmacogenomic test. |
| 7 | `MED_USE_NARRATIVE` | VARCHAR |  | Stores a free text comment describing the recommended alteration to medication based on the reported drug-gene interaction. |
| 8 | `MED_USE_CATEGORY_C_NAME` | VARCHAR |  | Stores a category value corresponding to the recommended alteration to medication based on the reported drug-gene interaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GNOM_INTPRT_ID` | [GNOM_INTPRT_IDENT](GNOM_INTPRT_IDENT.md) | sole_pk | high |

