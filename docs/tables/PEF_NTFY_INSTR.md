# PEF_NTFY_INSTR

> This table contains information on patient-entered flowsheet notification instructions and dates. Also contains settings for this episode that are related to tasks or flowsheets.

**Primary key:** `EPISODE_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the summary/episode block record. |
| 2 | `PEF_PAT_SPEC_INSTR` | VARCHAR |  | This item stores patient specific instructions |
| 3 | `PEF_SNOOZE_ALRT_YN` | VARCHAR |  | This item stores a flag to disable or enable sending patient-entered flowsheet alert messages while the patient is on Care Companion home monitoring. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

