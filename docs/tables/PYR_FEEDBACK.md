# PYR_FEEDBACK

> This table contains information about feedback shared via Payer Platform.

**Primary key:** `FEEDBACK_ID`  
**Columns:** 8  
**Org-specific columns:** 1  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FEEDBACK_ID` | NUMERIC | PK | The unique identifier (.1 item) for the Payer Platform feedback record. |
| 2 | `RECORD_STATUS_2_C_NAME` | VARCHAR |  | The record status of the Payer Platform feedback record. |
| 3 | `SRC_ORGANIZATION_ID` | NUMERIC |  | The unique ID of the data exchange organization that sent the feedback. |
| 4 | `SRC_ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 5 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient for which this feedback applies. This column is frequently used to link to the PATIENT table. |
| 6 | `ENC_TYPE_C_NAME` | VARCHAR | org | The encounter type category ID for the feedback record. |
| 7 | `ENC_DATE` | DATETIME |  | The date of the patient contact at the organization providing feedback. |
| 8 | `ENC_TIN` | VARCHAR |  | The tax ID for the patient encounter at the organization providing feedback. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [PYR_FEEDBACK_PAT_INSIGHT](PYR_FEEDBACK_PAT_INSIGHT.md) | `FEEDBACK_ID` | high |

