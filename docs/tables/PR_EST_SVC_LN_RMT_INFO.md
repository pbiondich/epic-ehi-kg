# PR_EST_SVC_LN_RMT_INFO

> Contains the adjudication information for each service line in a member estimate.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the patient estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADDL_LINE_NUM` | INTEGER |  | The line number of related group 1000 that stores additional information about the charge line. It is used to map a line in 2000 related group to a procedure line. |
| 4 | `FILE_ORD_NUM` | INTEGER |  | The coverage level associated with the corresponding coverage (I PES 168). |
| 5 | `REMIT_CODE_ID` | VARCHAR | FK→ | This stores any Explanation of Benefits/Remittance Advice codes associated with the service line. |
| 6 | `REMIT_CODE_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 7 | `REMIT_AMT` | NUMERIC |  | This stores the amount associated with the Explanation of Benefits or remittance advice codes. |
| 8 | `REMIT_CATEGORY_C_NAME` | VARCHAR |  | This stores the payment category that the payer has assigned the amount to |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REMIT_CODE_ID` | [CLARITY_RMC](CLARITY_RMC.md) | sole_pk | high |

