# PAT_ENC_CALL_PRPTS

> This table traces the Prompts (LPQ) records followed in the Protocol during clinical calls.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LINE` | INTEGER | PK | The line number for the patient call prompts. |
| 2 | `CONTACT_DATE` | DATETIME |  | The date for the encounter in standard date format. |
| 3 | `CLICKED_LPQS_PROMPT_NAME` | VARCHAR |  | The display name of the prompt record. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 5 | `CLICKED_USER_ID` | VARCHAR |  | User who clicked the corresponding prompt in CLICKED_LPQS column |
| 6 | `CLICKED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `PROMPT_CLICKED_DTTM` | DATETIME (UTC) |  | Instant when the user in CLICKED_USER_ID clicked the prompt in CLICKED_LPQs column. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

