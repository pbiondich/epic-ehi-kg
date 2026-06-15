# TARGET_TASK_ASMTS

> This table stores the patient encounters and assessments for target progress assessments.

**Primary key:** `ACTIVITY_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACTIVITY_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the task record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TARGET_PAT_ENC_CSN_ID` | NUMERIC | FK→ | This item stores the patient CSNs of the target assessments. |
| 4 | `TARGET_OVERALL_ASMT_C_NAME` | VARCHAR |  | This item stores the overall assessments of the target assessments. |
| 5 | `TARGET_PROG_ASMT_C_NAME` | VARCHAR |  | This item stores the progression assessments of the target assessments. |
| 6 | `TARGET_ASSESSED_INST_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instants that the user most recently assessed the target over different encounters. |
| 7 | `TARGET_ASSESSED_USER_ID` | VARCHAR |  | This item stores the users that most recently assessed the target over different encounters. |
| 8 | `TARGET_ASSESSED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `TARGET_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

