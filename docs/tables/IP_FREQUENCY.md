# IP_FREQUENCY

> This table contains data on discrete frequency (EFQ) records.

**Primary key:** `FREQ_ID`  
**Columns:** 2  
**Joined by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FREQ_ID` | VARCHAR | PK | The unique ID for the frequency record. |
| 2 | `FREQ_NAME` | VARCHAR |  | The name of the frequency record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (5)

| From | Column | Confidence |
|------|--------|------------|
| [POC_MEDICATIONS](POC_MEDICATIONS.md) | `FREQ_ID` | high |
| [TASK_LOG](TASK_LOG.md) | `FREQ_ID` | high |
| [TASK_PATIENT_ACTIVITY](TASK_PATIENT_ACTIVITY.md) | `FREQ_ID` | high |
| [TREATMENT_PLAN](TREATMENT_PLAN.md) | `FREQ_ID` | high |
| [TREATMENT_PLAN_AUDIT](TREATMENT_PLAN_AUDIT.md) | `FREQ_ID` | high |

