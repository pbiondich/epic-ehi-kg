# SERVICE_PLAN

> The SERVICE_PLAN table contains high-level information about service plans. Most workflow-related information in PLN is overtime and found in the SERVICE_PLAN_VERSION table.

**Primary key:** `SERVICE_PLAN_ID`  
**Columns:** 5  
**Joined by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SERVICE_PLAN_ID` | NUMERIC | PK | The unique identifier (.1 item) for the service plan record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc...). Category values are stored in table ZC_RECORD_STATUS_2. |
| 3 | `COMMENT_NOTE_ID` | VARCHAR |  | The note record that contains comments for all versions of the service plan. |
| 4 | `RECORD_CREATION_DATE` | DATETIME |  | Stores the date the record was created |
| 5 | `PAT_ID` | VARCHAR | FK→ | The ID of the patient to whom this plan belongs. This value is populated for plans associated with a Compass Rose episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (4)

| From | Column | Confidence |
|------|--------|------------|
| [SERVICE_PLAN_HX_CHANGE](SERVICE_PLAN_HX_CHANGE.md) | `SERVICE_PLAN_ID` | high |
| [SERVICE_PLAN_HX_REVISION](SERVICE_PLAN_HX_REVISION.md) | `SERVICE_PLAN_ID` | high |
| [SERVICE_PLAN_VERSION](SERVICE_PLAN_VERSION.md) | `SERVICE_PLAN_ID` | high |
| [SERVICE_PLAN_VISIT_SET](SERVICE_PLAN_VISIT_SET.md) | `SERVICE_PLAN_ID` | high |

