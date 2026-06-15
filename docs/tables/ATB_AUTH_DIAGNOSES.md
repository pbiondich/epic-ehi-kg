# ATB_AUTH_DIAGNOSES

> This table contains information pertaining to the diagnosis information for an Auth Bundle.

**Primary key:** `AUTH_BUNDLE_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the auth bundle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUTH_DX_REF_ID` | VARCHAR |  | The reference ID number that uniquely identifies this diagnosis on an authorization. |
| 4 | `AUTH_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 5 | `AUTH_PA_DX_TYPE_C_NAME` | VARCHAR |  | The Diagnosis Type category ID associated with the diagnosis on this line. |
| 6 | `AUTH_DX_DATE` | DATETIME |  | The date associated with this diagnosis, usually meaning the first date on which this diagnosis is applicable. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

