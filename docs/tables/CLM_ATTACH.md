# CLM_ATTACH

> All values associated with a claim are stored in the Claim External Value record. The CLM_ATTACH table holds information about attachments sent to the payor.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the Claim Info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `CLM_ATTACH_TYP` | VARCHAR |  | This item holds a code indicating the type of attachment being sent in support of the claim. |
| 4 | `CLM_ATTACH_CD` | VARCHAR |  | This item holds a code representing the method by which the attachment is transmitted to the payor. |
| 5 | `CLM_ATTACH_DCN` | VARCHAR |  | This item holds the document control number (DCN) for each attachment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

