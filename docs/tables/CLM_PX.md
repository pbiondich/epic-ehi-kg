# CLM_PX

> All values associated with a claim are stored in the Claim External Value record. The CLM_PX table holds the ICD procedures that document surgical procedures on inpatient claims.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique ID for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `CLM_PX_QUAL` | VARCHAR |  | The qualifier identifying the code set for the International Classification of Diseases (ICD) procedures. |
| 4 | `CLM_PX` | VARCHAR |  | The International Classification of Diseases (ICD) procedures for the claim. The principal procedure is stored on the first line and the other procedures are on subsequent lines. |
| 5 | `CLM_PX_DT` | DATETIME |  | The date of the International Classification of Diseases (ICD) procedure. |
| 6 | `CLM_PX_DESC` | VARCHAR |  | The text description for an International Classification of Diseases (ICD) procedure. |
| 7 | `CLM_PX_RANK` | INTEGER |  | The rank of this International Classification of Diseases (ICD) procedure compared to the other ICD procedures on the claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

