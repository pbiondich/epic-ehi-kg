# CHARGE_COUNT_IGNORED_MODS

> Stores the Modifiers which, if present on a charge linked to the Authorization, will cause the charge to not count towards the Authorization.

**Primary key:** `AUTH_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_ID` | NUMERIC | PK FK→ | The authorization ID for the authorization record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IGNMODS_MODIFIER_ID` | VARCHAR |  | Stores the list of Modifiers (MOD records) to be ignored for charge counting based on the charge counting configuration in the system (I POS 8035) for the corresponding RFL and CVG. This item would be set upon creation of Authorization (AUT) and will not be updated once set. If the Referral (RFL) record or coverage (CVG) corresponding to the Authorization is not using charge counting, this item would be empty. |
| 4 | `IGNMODS_MODIFIER_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_ID` | [AUTHORIZATIONS](AUTHORIZATIONS.md) | overflow_master | medium |

