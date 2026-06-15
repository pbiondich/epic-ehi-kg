# PAT_RSN_VISIT_DX

> All values associated with a claim are stored in the Claim External Value record. The PAT_RSN_VISIT_DX table holds the diagnoses that document the patient's reason for an outpatient visit.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_RSN_VISIT_QUAL` | VARCHAR |  | This item holds the qualifier identifying the code set for the patient reason for visit diagnoses. |
| 4 | `PAT_RSN_VISIT_DX` | VARCHAR |  | This item holds the diagnoses representing the patient's reason for the visit. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

