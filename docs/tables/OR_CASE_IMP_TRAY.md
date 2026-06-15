# OR_CASE_IMP_TRAY

> This table contains the implant trays information for the surgical case (ORC) record.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique ID of the procedural case record. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `IMP_TRAY_ID` | NUMERIC |  | Specifies the implant trays to be used in this surgery. |
| 4 | `IMP_TRAY_ID_RECORD_NAME` | VARCHAR |  | Name of the implant tray |
| 5 | `IMP_TRAY_DEFAULT_YN` | VARCHAR |  | Specifies whether this implant tray was defaulted by the system, or added/edited by the user. |
| 6 | `IMPL_TRAY_REQ_YN` | VARCHAR |  | Holds whether the implant tray is required |
| 7 | `IMP_TRAY_CMT` | VARCHAR |  | A free-text comment about an implant tray. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

