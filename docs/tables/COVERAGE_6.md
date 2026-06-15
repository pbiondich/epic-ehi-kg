# COVERAGE_6

> The COVERAGE_6 table contains high-level information on both managed care and indemnity coverage records in your system.

**Overflow of:** [COVERAGE](COVERAGE.md)  
**Primary key:** `COVERAGE_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK | The unique identifier (.1 item) for the coverage record. |
| 2 | `ORIGINAL_BINDER_COVERAGE_ID` | NUMERIC |  | The unique ID of the first coverage in the chain of coverages that this coverage shares its binder payment with. |
| 3 | `REDETERMINATION_DATE` | DATETIME |  | The date when the patient’s coverage must undergo redetermination or recertification to assess continued eligibility. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [COVERAGE](COVERAGE.md).

