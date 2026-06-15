# CVG_REL_OF_INFO

> The CVG_REL_OF_INFO table contains a list of release of information data that has been received for members on a coverage.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique ID assigned to the coverage record. This ID may be encrypted if you have elected to use enterprise reporting’s encryption utility. |
| 2 | `LINE` | INTEGER | PK | The line number of release of information on the coverage. |
| 3 | `ROI_PAT_ID` | VARCHAR | FK→ | The unique patient ID associated with the release of information. |
| 4 | `ROI_CONSENT_C_NAME` | VARCHAR | org | The status of the member's release of information. |
| 5 | `ROI_EFF_DATE` | DATETIME |  | The effective date of the release of information for a member on the coverage. |
| 6 | `ROI_TERM_DATE` | DATETIME |  | The termination date of the release of information for a member on the coverage. |
| 7 | `ROI_SOURCE_DOC_C_NAME` | VARCHAR | org | The source document associated with the release of information for a member on the coverage. |
| 8 | `ROI_DOC_DATE` | DATETIME |  | The date of the source document associated with the release of information for a member on the coverage. |
| 9 | `ROI_COMMENT` | VARCHAR |  | The free text comment associated with the release of information for a member on the coverage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `ROI_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

