# CLARITY_IMMUNZATN

> The CLARITY_IMMUNZATN table contains high-level information about the immunizations providers can choose on the Immunization Administration window. These records should not be confused with the actual immunization procedures.

**Primary key:** `IMMUNZATN_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMMUNZATN_ID` | NUMERIC | PK | The unique ID of the immunization record. |
| 2 | `IMMUNZATN_ID_NAME` | VARCHAR |  | The name of the immunization. |
| 3 | `NAME` | VARCHAR |  | The name of the immunization. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [IMMUNE](IMMUNE.md) | `IMMUNZATN_ID` | high |

