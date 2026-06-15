# REI_LAB_PROCS

> Contains a list of lab procedures for the fertility treatment cycle. This option can be set by end users only when the cycle's version is 1 or greater (INFERTILITY_CYCLE.REI_CYCLE_VERSION_C, Chronicles item ICF-86991).

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the cycle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LAB_PROC_C_NAME` | VARCHAR | org | This item stores a list of laboratory procedures that were done for this treatment cycle. For procedures that were done to the patient, see table REI_ART_PROCS and I ICF 86303. This item will only be available when the Version (INFERTILITY_CYCLE.REI_CYCLE_VERSION_C, Chronicles item I ICF 86991) is 1 or greater. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

