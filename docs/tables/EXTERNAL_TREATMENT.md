# EXTERNAL_TREATMENT

> This represents a medication treatment that is shared with external systems.

**Primary key:** `MED_PRBLM_LIST_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MED_PRBLM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the med problem list record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORDER_MED_ID` | NUMERIC | FK→ | Stores the ORD which this external treamtent is stored in |
| 4 | `TREATMENT_IDENT` | VARCHAR |  | The external treatment identifier |
| 5 | `EXTERNAL_ORDER_IDENT` | VARCHAR |  | The external order ID |
| 6 | `DISPENSE_REQUEST_IDENT` | VARCHAR |  | The external dispense request ID |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MED_PRBLM_LIST_ID` | [MDL_MD_PRBLM_LIST](MDL_MD_PRBLM_LIST.md) | sole_pk | high |
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

