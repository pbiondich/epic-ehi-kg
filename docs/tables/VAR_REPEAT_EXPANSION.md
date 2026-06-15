# VAR_REPEAT_EXPANSION

> This table stores information about repeat expansion variants, including the repeated nucleotides and the number of times the nucleotides are repeated.

**Primary key:** `VARIANT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VARIANT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the variant record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REPEAT_NUCLEOTIDES` | VARCHAR |  | The sequence of the nucleotides in a single unit of the repeat expansion variant. |
| 4 | `REPEAT_NUMBER` | INTEGER |  | The number of times a sequence of nucleotides (in REPEAT_NUCLEOTIDES) is repeated. |
| 5 | `REPEAT_NUMBER_LEADING` | INTEGER |  | Repeat number is to record the repeated number in repeat expansion variant. For structured numeric values, this is the number used with the operator (or leading number if there is a range). |
| 6 | `REPEAT_NUMBER_TRAILING` | INTEGER |  | Repeat number is to record the repeated number in repeat expansion variant. For structured numeric values, this is the upper bound value if there is a range. Otherwise, this item is not populated. |
| 7 | `RPT_NUM_COMPARE_OPERATO_C_NAME` | VARCHAR |  | Repeat number is to record the repeated number in repeat expansion variant. For structured numeric values, this is the relevant operator to use with the leading and trailing number related items. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VARIANT_ID` | [VARIANT](VARIANT.md) | sole_pk | high |

