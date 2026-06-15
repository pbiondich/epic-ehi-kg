# UCL_DOC_PROVIDER

> The UCL_DOC_PROVIDER table contains information about the documentation providers for universal charge records.

**Primary key:** `UCL_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `UCL_ID` | VARCHAR | PK FK→ | The unique ID associated with the charge record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DOC_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `DOC_PROV_FUNC_C_NAME` | VARCHAR | org | The documentation provider's function for this procedure. |
| 5 | `DOC_PROV_ST_DT_TM` | DATETIME (Local) |  | The start date and time for the documentation provider for this procedure. |
| 6 | `DOC_PROV_ED_DT_TM` | DATETIME (Local) |  | The end date and time for the documentation provider for this procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `UCL_ID` | [CLARITY_UCL](CLARITY_UCL.md) | sole_pk | high |

