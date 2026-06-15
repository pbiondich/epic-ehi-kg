# TREATMENT_CLASS

> The TREATMENT_CLASS table contains information about how your treatment class records are built.

**Primary key:** `TREATMENT_CLASS_ID`  
**Columns:** 2  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_CLASS_ID` | NUMERIC | PK | The unique identifier (.1 item) for the treatment class record. |
| 2 | `DISPLAY_NAME` | VARCHAR |  | The name of the treatment class that is displayed to end users. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [INTERVENTIONS_HISTORY](INTERVENTIONS_HISTORY.md) | `TREATMENT_CLASS_ID` | high |
| [INTVTN_CONTACT](INTVTN_CONTACT.md) | `TREATMENT_CLASS_ID` | high |
| [REMOVED_TREATMENT_CLASS](REMOVED_TREATMENT_CLASS.md) | `TREATMENT_CLASS_ID` | high |

