# BENEFITS

> The BENEFITS table contains information specific to benefits collection (BEN) record.

**Primary key:** `RECORD_ID`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the benefit record. |
| 2 | `ENC_BENEFIT_VRX_ID` | NUMERIC |  | The verification record for the encounter's benefits. |
| 3 | `RECORD_CREATION_DT` | DATETIME |  | The date the record was created. |
| 4 | `PAT_ID` | VARCHAR | FK→ | Patient ID |
| 5 | `VERIFICATION_DATE` | DATETIME |  | The most recent verification date of this BEN record. This will be used to facilitate easier BEN record searching in the future. |
| 6 | `ORIG_VERIFICATION_DATE` | DATETIME |  | The original verification date of the data on this BEN record when it was entered manually or by RTE and verified for the first time. |
| 7 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record's status. |
| 8 | `BENEFIT_PERIOD_COVERAGE_ID` | NUMERIC |  | Only populated on coverage-level benefits records. The record ID of the coverage associated with this benefit record. |
| 9 | `BENEFIT_PERIOD_START_DATE` | DATETIME |  | The start date for the benefits on this record. Only populated on coverage benefit records. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

