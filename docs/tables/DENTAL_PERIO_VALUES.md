# DENTAL_PERIO_VALUES

> This table contains information documented during a patient's periodontal exam, such as probing depths or gingival margin readings.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DENTAL_PROBE_DEPTH` | NUMERIC |  | Stores the probing depth measurements (in millimeters) taken for a tooth during a periodontal exam |
| 4 | `DENTAL_GING_MARGIN` | NUMERIC |  | Stores the gingival margin measurements (in millimeters) taken for a tooth during a periodontal exam |
| 5 | `DENT_PERIO_LOC_C_NAME` | VARCHAR | org | Stores the location of various periodontal data points. |
| 6 | `DENTAL_CLIN_ATT_LVL` | NUMERIC |  | Stores the clinical attachment level measurements (in millimeters) taken for a tooth during a periodontal exam |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

