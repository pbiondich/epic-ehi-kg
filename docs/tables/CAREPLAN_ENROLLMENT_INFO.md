# CAREPLAN_ENROLLMENT_INFO

> This table cotains the enrollment information for a care plan.

**Primary key:** `CAREPLAN_ID`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CAREPLAN_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the care plan record. |
| 2 | `CP_ENROLL_WORKFLOW_C_NAME` | VARCHAR |  | This item store the Care Companion workflow from where this care plan was applied to the patient. |
| 3 | `ALERT_CSN_ID` | NUMERIC |  | OurPractice Advisory ALT CSN used to enroll the patient in the care plan. |
| 4 | `SIGNUP_MYPT_ID` | VARCHAR |  | MyChart user ID who enrolled the patient in the care plan. |
| 5 | `PREG_SELF_EPISODE_ID` | NUMERIC |  | Pregnancy episode ID (HSB) associated with the self-enrolled care plan. |
| 6 | `ENROLLING_USER_ID` | VARCHAR |  | User who enrolled the patient in the care plan. |
| 7 | `ENROLLING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `SURGICAL_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Patient CSN linked to the surgical encounter where the enrollment was done |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SURGICAL_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

