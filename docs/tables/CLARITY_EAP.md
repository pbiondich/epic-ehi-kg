# CLARITY_EAP

> The CLARITY_EAP table contains basic information about the procedure records in your system. This does include both A/R and clinical procedures.

**Overflow family:** [CLARITY_EAP_3](CLARITY_EAP_3.md), [CLARITY_EAP_5](CLARITY_EAP_5.md)  
**Primary key:** `PROC_ID`  
**Columns:** 2  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 2 | `PROC_NAME` | VARCHAR |  | The name of each procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [OR_CASE_QUEST_AN_P](OR_CASE_QUEST_AN_P.md) | `PROC_ID` | high |
| [OR_LOG_QUEST_AN_P](OR_LOG_QUEST_AN_P.md) | `PROC_ID` | high |

