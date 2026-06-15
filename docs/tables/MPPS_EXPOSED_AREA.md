# MPPS_EXPOSED_AREA

> This table contains dimensions of the area exposed during the modality performed procedure step.

**Primary key:** `IMY_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMY_ID` | NUMERIC | PK shared | The unique identifier for the modality data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DIMENSION` | NUMERIC |  | Typical dimension of the exposed area at the detector plane. If Rectangular: row dimension followed by column; if Round: diameter. Measured in mm. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

