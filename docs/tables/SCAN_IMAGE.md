# SCAN_IMAGE

> Provides information about coverage scans.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique ID assigned to the coverage record. This ID may be encrypted if you have elected to use enterprise reporting’s encryption utility. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SCAN_IMAGE_FILE` | VARCHAR |  | The path where the scanned image is stored. |
| 4 | `SCAN_DESC` | VARCHAR |  | The free-text description associated with the scanned image. |
| 5 | `DEPT_WHERE_SCAND_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 6 | `DATE_OF_SCAN_DT` | DATETIME |  | The date that the image was scanned. |
| 7 | `SCAN_IMAGE_TYPE_C_NAME` | VARCHAR | org | The Scan Image Type category number for the scanned document. Only coverage level scans have a value populated for this column. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

