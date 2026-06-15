# SPECIMEN_CYCLES

> The fertility treatment cycles that are associated with oocyte, embryo, or sperm specimens. For example, an embryo can be linked to an egg retrieval/freeze cycle and also a thaw/embryo transfer cycle.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CYCLE_ID` | NUMERIC | FK→ | The fertility treatment cycles that are associated with the fertility specimen. This includes the cycle that the oocyte or embryo was retrieved on, transferred, frozen, or thawed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CYCLE_ID` | [INFERTILITY_CYCLE](INFERTILITY_CYCLE.md) | sole_pk | high |

