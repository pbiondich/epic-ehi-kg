# QRY_SUGGESTION_INFO

> This table extracts the suggested diagnosis code and the text description of the diagnosis suggestion for a query.

**Primary key:** `QUERY_CSN_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `QUERY_ID` | NUMERIC | FK→ | The unique identifier for the query record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `SUGGESTION_NAME` | VARCHAR |  | The display name of the suggested code. |
| 5 | `SUGGESTION_PRIM_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 6 | `SUGGESTION_ALT_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 7 | `SUGGESTION_TEXT` | VARCHAR |  | The text prompt of the suggestion. |
| 8 | `SUGGESTION_SELECT_YN` | VARCHAR |  | Whether the suggestion has been selected by the physician. |
| 9 | `QUERY_CSN_ID` | NUMERIC | PK FK→ | The contact serial number (CSN) of the contact. |
| 10 | `SUGGESTION_TERM_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `QUERY_CSN_ID` | [QRY_CONTACT_INFO](QRY_CONTACT_INFO.md) | sole_pk | high |
| `QUERY_ID` | [QRY_RECORD_INFO](QRY_RECORD_INFO.md) | sole_pk | high |

