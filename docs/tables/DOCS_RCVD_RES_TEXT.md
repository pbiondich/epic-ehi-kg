# DOCS_RCVD_RES_TEXT

> The DOCS_RCVD_RES_TEXT table contains textual information about a result.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | Stores the Received Document record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `RES_TEXT_KEY_CMP` | VARCHAR |  | The key which links the result text with the order. |
| 4 | `RES_TEXT_COMPILED` | VARCHAR |  | A line of text for the result. |
| 5 | `RES_TEXT_CAT_CMP_C_NAME` | VARCHAR |  | The internal category identifying what kind of textual information is recorded in this line. |
| 6 | `RES_TEXT_SUBID_CMP` | VARCHAR |  | A key used to identify different entries for multiple results of the same type. Lines may match the same result key but will have different sub IDs to identify them as different records. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

