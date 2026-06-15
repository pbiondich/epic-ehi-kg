# TYMPANOGRAM_DATA

> Contains all related data for Tympanograms.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TYMP_EAR_C_NAME` | VARCHAR |  | Stores which ear the Tympanometry procedure was performed |
| 4 | `TYMP_TYPE_C_NAME` | VARCHAR | org | Stores the type of the tympanogram based on the shape of the graph. |
| 5 | `CANAL_VOLUME` | NUMERIC |  | Stores the ear canal volume which is measured by the Tympanometer |
| 6 | `PEAK_PRESSURE` | NUMERIC |  | Stores the peak pressure for the Tympanogram |
| 7 | `PEAK_AMPLITUDE` | NUMERIC |  | Stores the peak amplitude for the Tympanogram |
| 8 | `TYMP_WIDTH` | NUMERIC |  | Stores the Tympanogram width |
| 9 | `BURNED_IMAGE` | VARCHAR |  | Blob key of burned image of tympanogram drawing |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

