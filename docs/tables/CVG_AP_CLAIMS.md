# CVG_AP_CLAIMS

> This table contains coverage information generated and owned by AP Claims adjudication. If your organization uses a separate AP Claims instance in an Interconnect setting, then this table should be extracted from the AP Claims instance instead of the clinical instance.

**Primary key:** `COVERAGE_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `HIX_CSR_SRC_CVG_ID` | NUMERIC |  | This column is used to identify Cost Sharing Reduction (CSR) coverages and their corresponding source coverage record. The value stored in this column is the ID of the source coverage of this CSR coverage. If the value is null, this coverage is not a CSR coverage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

