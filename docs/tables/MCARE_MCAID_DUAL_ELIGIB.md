# MCARE_MCAID_DUAL_ELIGIB

> This table contains the Medicare-Medicaid dual eligibility statuses for patients.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MCARE_MCAID_DUAL_STAT_C_NAME` | VARCHAR |  | The Medicare and Medicaid dual eligibility status category ID for the patient. |
| 4 | `MCARE_MCAID_DUAL_START_DATE` | DATETIME |  | The date when the patient's Medicare and Medicaid dual eligibility status starts. |
| 5 | `MCARE_MCAID_DUAL_END_DATE` | DATETIME |  | The date when the patient's Medicare and Medicaid dual eligibility status ends. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

