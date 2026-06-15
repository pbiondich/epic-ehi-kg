# CHRG_TRIG_MTHD

> No-add single information for the LCM masterfile.

**Primary key:** `CHRG_METHOD_ID`  
**Columns:** 3  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CHRG_METHOD_ID` | VARCHAR | PK | The unique ID of the charge trigger method record. |
| 2 | `CHRG_METHOD_ID_CHRG_METHOD_NAME` | VARCHAR |  | The name of the charge trigger method. |
| 3 | `CHRG_METHOD_NAME` | VARCHAR |  | The name of the charge trigger method. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [ORDER_PROC_2](ORDER_PROC_2.md) | `CHRG_METHOD_ID` | high |
| [SPEC_TEST_REL](SPEC_TEST_REL.md) | `CHRG_METHOD_ID` | high |

