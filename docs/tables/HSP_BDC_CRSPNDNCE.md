# HSP_BDC_CRSPNDNCE

> Correspondence text in a Denial/Correspondence (BDC) record. Stores the lines of correspondence text received.

**Primary key:** `BDC_ID`, `LINE_COUNT`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BDC_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the denial or correspondence record. |
| 2 | `LINE_COUNT` | INTEGER | PK | Line number of correspondence text that is being extracted by enterprise reporting |
| 3 | `CRSPNDCE_TEXT` | VARCHAR |  | This column stores the one line of Correspondence Text or Comments (I BDC 300). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BDC_ID` | [BDC_INFO](BDC_INFO.md) | sole_pk | high |

