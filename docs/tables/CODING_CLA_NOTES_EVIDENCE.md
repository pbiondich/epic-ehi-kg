# CODING_CLA_NOTES_EVIDENCE

> This table extracts evidence-related information (such as vitals, medication, results) tied to a query.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `QRY_EVIDENCE_TYPE_C_NAME` | VARCHAR |  | The type of evidence that support the suggestion of the query. |
| 4 | `EVIDENCE_NAME` | VARCHAR |  | The display name of the evidence to support the suggestion of the query. This can range from the lab result to an excerpt from a clinical note. |
| 5 | `EVIDENCE_SOURCE_C_NAME` | VARCHAR |  | The source of evidence that support the suggestion of the query. |
| 6 | `EVID_MENTIONED_YN` | VARCHAR |  | List of 0's and 1's indicating which of the AI-generated evidence the user chose to include in the query. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

