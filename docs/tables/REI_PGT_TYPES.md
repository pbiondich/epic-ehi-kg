# REI_PGT_TYPES

> This stores the types of preimplantation genetic testing (PGT) that will be done for a fertility treatment cycle. This option is available only when the cycle's version is 2 or greater (INFERTILITY_CYCLE.REI_CYCLE_VERSION_C, Chronicles item ICF-86991).

**Primary key:** `CYCLE_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CYCLE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the cycle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REI_PGT_TYPE_C_NAME` | VARCHAR | org | The types of preimplantation genetic testing done for the cycle. This item is available only when the Version (INFERTILITY_CYCLE.REI_CYCLE_VERSION_C, Chronicles item ICF-86991) is 2 or greater. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CYCLE_ID` | [INFERTILITY_CYCLE](INFERTILITY_CYCLE.md) | sole_pk | high |

