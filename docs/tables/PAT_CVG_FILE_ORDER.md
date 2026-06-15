# PAT_CVG_FILE_ORDER

> The PAT_CVG_FILE_ORDER table contains information about the filing order of each member's coverages. Since members can have multiple coverages, each row of coverage filing order information in this table is identified by the patient ID and a line number.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting’s encryption utility. |
| 2 | `LINE` | INTEGER | PK | The line number used to identify each line of filing order information for the patient. |
| 3 | `COVERAGE_ID` | NUMERIC | FK→ | The unique ID assigned to the coverage record. This ID may be encrypted if you have elected to use enterprise reporting’s encryption utility. |
| 4 | `FILING_ORDER` | INTEGER |  | The coverage filing order, as determined manually by a user or automatically using the automatic filing order rules. |
| 5 | `FILING_ORDER_CAT` | VARCHAR |  | This field will contain the abbreviation Spec if the coverage has a relative filing order; for example, a worker’s comp coverage would have a filing order of Special so that coverage would be consulted first when working with worker’s comp related charges. |
| 6 | `HOSP_FILE_ORD` | INTEGER |  | The coverage filing order pertaining to inpatient charges. This column only contains data if you are using Epic’s ADT or inpatient applications. |
| 7 | `HOSP_FILE_ORD_CAT` | VARCHAR |  | This column only contains data if you are using Epic’s ADT or inpatient applications. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

