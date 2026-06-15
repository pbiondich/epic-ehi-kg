# AN_HSB_LINK_PROCS

> For use with anesthesia, stores all patient encounters (procedure cases, appointments) that are linked to by (fall under the sedation of) the anesthesia episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the Episode. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EPT_PROC_CSN` | NUMERIC |  | Provides the patient encounter contact serial numbers (CSNs) for procedures linked to the anesthesia episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

