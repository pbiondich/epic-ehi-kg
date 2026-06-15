# CLARITY_HVR

> This table contains information about the generic verification (HVR) record.

**Primary key:** `VERIFY_ID`  
**Columns:** 9  
**Org-specific columns:** 1  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VERIFY_ID` | NUMERIC | PK | The unique ID of the verification record |
| 2 | `REC_STAT_C_NAME` | VARCHAR |  | Record status flag special item. Indicates whether the verification record is active, deleted, hidden, or a combination of statuses. |
| 3 | `VERIFY_TYPE_C_NAME` | VARCHAR | org | Category value representing the type of verification performed. |
| 4 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient associated with the verification record. |
| 5 | `PAT_CSN_ID` | NUMERIC |  | The Contact Serial Number of the patient encounter the verification was performed within. |
| 6 | `LOG_ID` | VARCHAR | shared | Surgical log ID for this verification record. |
| 7 | `VERIFY_USER_ID` | VARCHAR |  | The unique ID of the user who performed the verification |
| 8 | `VERIFY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `VERIFY_INSTANT` | DATETIME (Attached) |  | The instant the verification was performed |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [CLARITY_HVR_ANSWER](CLARITY_HVR_ANSWER.md) | `VERIFY_ID` | high |
| [CLARITY_HVR_SDFL](CLARITY_HVR_SDFL.md) | `VERIFY_ID` | high |

