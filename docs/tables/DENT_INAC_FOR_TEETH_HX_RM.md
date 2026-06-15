# DENT_INAC_FOR_TEETH_HX_RM

> History of teeth which are considered inactive for procedures and findings in the tooth chart.

**Primary key:** `FINDING_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the historical instant in the procedure record. Together with FINDING_ID, this forms the foreign key to the DENTAL_PROC_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple inactive teeth associated with the procedure record and the historical instant from the DENTAL_PROC_HX table. |
| 4 | `DENT_INACT_HX_ID` | NUMERIC |  | Tracks the audit history of the inactive teeth for dental findings and procedures. "Inactive teeth" refers to teeth where the finding/procedure is no longer clinically relevant, so does not display on the Tooth Chart for those teeth |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

