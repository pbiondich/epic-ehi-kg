# AUTH_REQ_GUIDELINE_VENDOR

> The guideline review vendors as AGY IDs that are used for the guideline review process for the authorization request.

**Primary key:** `AUTH_REQUEST_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_REQUEST_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the authorization request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `GUIDELINE_REVIEW_AGENCY_ID` | VARCHAR |  | The guideline review vendors as AGY IDs that are used for the guideline review process for the authorization request. |
| 4 | `GUIDELINE_REVIEW_AGENCY_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_REQUEST_ID` | [AUTH_REQUEST](AUTH_REQUEST.md) | sole_pk | high |

