# UCL_AMBRX_COVERAGE

> This table contains information about coverages and their promised payment data for universal charge records. The table references the Rx - Coverage ID (I UCL 1111), Rx - Authorization Number (I UCL 1112), Rx - Promised Payment Amount (I UCL 1113), Rx - Patient Due Amount (I UCL 1114), and Rx - Write-Off Amount (I UCL 1115) items in columns 5, 6, 7, 8, and 9 respectively. These items are used in the long term care module for pharmacy adjudication and copays. This table only displays data from records with a source of Ambulatory. To see all records, without this restriction, please see UCL_RX_COVERAGE.

**Primary key:** `UCL_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `UCL_ID` | VARCHAR | PK FK→ | The unique ID associated with the charge record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AMBRX_COVERAGE_ID` | NUMERIC |  | Stores the coverage for an Ambulatory Pharmacy charge. |
| 4 | `AMBRX_PROMISED_PMT` | NUMERIC |  | Stores the payment amount promised to the organization by the payor specified in the coverage. |
| 5 | `PAT_DUE_AMT` | NUMERIC |  | Stores the payment amount due to the organization from the patient for a pharmacy charge. |
| 6 | `WRITE_OFF_AMT` | NUMERIC |  | Stores the amount to be written off by the organization for a pharmacy charge. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `UCL_ID` | [CLARITY_UCL](CLARITY_UCL.md) | sole_pk | high |

