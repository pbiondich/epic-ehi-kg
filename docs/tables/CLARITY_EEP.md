# CLARITY_EEP

> This table contains information about employer records from the EEP master file.

**Primary key:** `EMPLOYER_ID`  
**Columns:** 3  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EMPLOYER_ID` | VARCHAR | PK | The unique ID for the employer record. |
| 2 | `EMPLOYER_ID_EMPLOYER_NAME` | VARCHAR |  | The name of the employer. |
| 3 | `EMPLOYER_NAME` | VARCHAR |  | The name of the employer. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [CASE_MGMT](CASE_MGMT.md) | `EMPLOYER_ID` | high |
| [PATIENT](PATIENT.md) | `EMPLOYER_ID` | high |

