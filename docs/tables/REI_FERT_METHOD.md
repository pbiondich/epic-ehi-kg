# REI_FERT_METHOD

> The REI_FERT_METHOD table contains information about the oocyte fertilization method used for fertility treatment cycles.

**Primary key:** `CYCLE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CYCLE_ID` | NUMERIC | PK FK→ | The unique identifier for the fertility treatment cycle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FERT_METHOD_C_NAME` | VARCHAR |  | The oocyte fertilization method. For assisted reproductive technology (ART) cycles, you can have in vitro fertilization (IVF), IVF with intra-cytoplasmic sperm injection (ICSI), or both. For non-ART fertility treatment cycles, you can have intrauterine insemination (IUI), timed intercourse, or therapeutic donor insemination (TDI) which would also be considered an IUI but with donor sperm. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CYCLE_ID` | [INFERTILITY_CYCLE](INFERTILITY_CYCLE.md) | sole_pk | high |

