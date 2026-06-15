# GNOM_INTPRT_IDENT

> Information about the identity of a genomic interpretation.

**Primary key:** `GNOM_INTPRT_ID`  
**Columns:** 4  
**Joined by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GNOM_INTPRT_ID` | NUMERIC | PK | The unique identifier (.1 item) for the interpretation record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | Stores the EPT ID of the patient associated with the interpretation. |
| 3 | `RQG_GROUPER_ID` | NUMERIC | FK→ | Stores the RQG ID of the non-enterprise patient associated with the interpretation. |
| 4 | `ACTIVE_YN` | VARCHAR |  | Indicates if this interpretation is part of the most recent contact of a finalized result on a patient's chart. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `RQG_GROUPER_ID` | [RQG_DB_MAIN](RQG_DB_MAIN.md) | sole_pk | high |

## Joined in — referenced by (8)

| From | Column | Confidence |
|------|--------|------------|
| [GNOM_INTPRT_CLASS_NARR](GNOM_INTPRT_CLASS_NARR.md) | `GNOM_INTPRT_ID` | high |
| [GNOM_INTPRT_EFFECTS](GNOM_INTPRT_EFFECTS.md) | `GNOM_INTPRT_ID` | high |
| [GNOM_INTPRT_HT_AUDIT](GNOM_INTPRT_HT_AUDIT.md) | `GNOM_INTPRT_ID` | high |
| [GNOM_INTPRT_MED_USE](GNOM_INTPRT_MED_USE.md) | `GNOM_INTPRT_ID` | high |
| [GNOM_INTPRT_ORDER_STATUS](GNOM_INTPRT_ORDER_STATUS.md) | `GNOM_INTPRT_ID` | high |
| [GNOM_INTPRT_PHENO_CODES](GNOM_INTPRT_PHENO_CODES.md) | `GNOM_INTPRT_ID` | high |
| [GNOM_INTPRT_VARIANTS](GNOM_INTPRT_VARIANTS.md) | `GNOM_INTPRT_ID` | high |
| [GNOM_INTPRT_VER_INFO](GNOM_INTPRT_VER_INFO.md) | `GNOM_INTPRT_ID` | high |

