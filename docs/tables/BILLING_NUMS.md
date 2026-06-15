# BILLING_NUMS

> Table containing ADT Billing Number information (EPT superitem 25000).

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record; each line represents a different billing account. |
| 3 | `BILLING_ACCT_NUM` | VARCHAR |  | The billing number for a patient's billing account. |
| 4 | `BILLING_ACCT_TYPE_C_NAME` | VARCHAR | org | The category number of the billing account type for the associated billing account. |
| 5 | `ADMIT_DATE` | DATETIME |  | The admission date for the associated billing account. |
| 6 | `DISCHARGE_DATE` | DATETIME |  | The discharge date for the associated billing account. |
| 7 | `BILLING_STATUS_C_NAME` | VARCHAR | org | The category number of the billing status for the associated billing account. |
| 8 | `BILLING_SERVICE_C_NAME` | VARCHAR | org | The category number of the billing service for the associated billing account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

