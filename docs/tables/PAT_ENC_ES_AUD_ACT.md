# PAT_ENC_ES_AUD_ACT

> The PAT_ENC_ES_AUD_ACT table contains scheduling system's auditing of actions taken on appointment contacts.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LINE` | INTEGER | PK | The number of audit lines for the patient and contact date. |
| 2 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 3 | `PAT_ONLINE_YN` | VARCHAR |  | Computed item that returns whether or not the audit source is considered to be from an online, patient or patient proxy initiated source. |
| 4 | `ACTING_MYPT_ID` | VARCHAR |  | The MyChart user who executed the action. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

