# ASST_SURG_SEC_ID

> All values associated with a claim are stored in the Claim External Value record. The ASST_SURG_SEC_ID table holds secondary (legacy) identifiers for the assistant dental surgeon.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `ASST_SURG_SEC_QUAL` | VARCHAR |  | This item holds a qualifier describing additional IDs used to identify the assistant dental surgeon. |
| 4 | `ASST_SURG_SEC_ID` | VARCHAR |  | This item holds additional IDs for the assistant dental surgeon. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

