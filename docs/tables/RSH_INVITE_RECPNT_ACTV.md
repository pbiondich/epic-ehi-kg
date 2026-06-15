# RSH_INVITE_RECPNT_ACTV

> This table contains whether each recipient of a research study invitation had an active MyChart account at the time the invitation was sent.

**Primary key:** `ENROLL_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the enrollment record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `INVITATION_MYC_ACTIVE_YN` | VARCHAR |  | Indicates whether the research study invitation recipient had an active MyChart account when the invitation was sent. 'Y' indicates that the recipient had an active MyChart account when the invitation was sent. 'N' or NULL indicates that the recipient did not have an active MyChart account when the invitation was sent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

