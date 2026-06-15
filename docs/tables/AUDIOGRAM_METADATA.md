# AUDIOGRAM_METADATA

> Contains values for metadata related to an Audiogram Exam. Including Technique, Transducer, Reliability, Baseline, and RSH ID.

**Primary key:** `FINDING_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `AUD_BASELINE_C_NAME` | VARCHAR |  | Item used to indicate what type of baseline an audiogram is. Options are: none, left, right, bilateral |
| 3 | `AUDIO_RELIABILITY_C_NAME` | VARCHAR |  | Represents how reliable the Audiogram results are. The possible responses are Good, Fair, or Poor. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

