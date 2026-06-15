# SMARTTEXT

> This table contains information relating to SmartText records. SmartTexts are blocks of text which may be used in a variety of ways, including documenting on clinical encounters, and for letters sent to patients.

**Primary key:** `SMARTTEXT_ID`  
**Columns:** 2  
**Joined by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SMARTTEXT_ID` | VARCHAR | PK | The ID of the SmartText record. |
| 2 | `SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (4)

| From | Column | Confidence |
|------|--------|------------|
| [DISC_SPECIFIC_INFO](DISC_SPECIFIC_INFO.md) | `SMARTTEXT_ID` | high |
| [IP_EDU_HANDOUT_TRACKING](IP_EDU_HANDOUT_TRACKING.md) | `SMARTTEXT_ID` | high |
| [IP_EDU_HANDOUT_TRACK_HX](IP_EDU_HANDOUT_TRACK_HX.md) | `SMARTTEXT_ID` | high |
| [TIMEOUT_ANSWERS_2](TIMEOUT_ANSWERS_2.md) | `SMARTTEXT_ID` | high |

