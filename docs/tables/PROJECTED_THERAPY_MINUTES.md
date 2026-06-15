# PROJECTED_THERAPY_MINUTES

> The PROJECTED_THERAPY_MINUTES table contains information about the Speech-Language Pathology, Occupational Therapy, and Physical Therapy minutes projections for a given resident in your Long Term Care facility.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `THERAPY_PROJECTION_DATE` | DATETIME |  | This item records the date for which a set of therapy projections applies. |
| 4 | `SLP_PROJECTED_MINUTES` | INTEGER |  | This item records the number of minutes projected for Speech-Language Pathology services on a given date. |
| 5 | `OT_PROJECTED_MINUTES` | INTEGER |  | This item records the number of minutes projected for Occupational Therapy services on a given date. |
| 6 | `PT_PROJECTED_MINUTES` | INTEGER |  | This item records the number of minutes projected for Physical Therapy services on a given date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

