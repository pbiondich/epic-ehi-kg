# PAT_ENC_MSP_WC

> This table contains the Worker's Compensation Info part of the Medicare Secondary Payor Information from the Patient (EPT) master file.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 2 | `CONTACT_DATE` | DATETIME |  | The date (calendar format) on which the encounter took place. |
| 3 | `WORKERS_COMP_YN` | VARCHAR |  | YES if the illness or injury is covered by a workers' compensation claim. |
| 4 | `WC_ACCDNT_DATE` | DATETIME |  | Injury date of the work related accident. |
| 5 | `WC_CLAIM_NUMBER` | VARCHAR |  | Worker's compensation claim number. |
| 6 | `WC_POLICY_NUMBER` | VARCHAR |  | Policy number of the workers' compensation coverage for the accident. |
| 7 | `WC_EMPLR_NAME` | VARCHAR |  | If the accident occurred at work, enter the place of employment. |
| 8 | `WC_EMPLR_ADR_1` | VARCHAR |  | Line 1 of worker's compensations' employer's street address. |
| 9 | `WC_EMPLR_ADR_2` | VARCHAR |  | Line 2 of worker's compensations' employer's street address. |
| 10 | `WC_EMPLR_CITY` | VARCHAR |  | Worker's compensation employer's city |
| 11 | `WC_EMPLR_ZIP` | VARCHAR |  | Worker's compensation employer's Zip. |
| 12 | `WC_PLAN_NAME` | VARCHAR |  | Worker's compensation insurance plan name. |
| 13 | `WC_PLAN_ADR_1` | VARCHAR |  | Line 1 of the street address for the worker's compensation plan. |
| 14 | `WC_PLAN_ADR_2` | VARCHAR |  | Line 2 of the street address for the worker's compensation plan. |
| 15 | `WC_PLAN_CITY` | VARCHAR |  | Insurance company's city. |
| 16 | `WC_PLAN_ZIP` | VARCHAR |  | Insurance company's ZIP Code |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

