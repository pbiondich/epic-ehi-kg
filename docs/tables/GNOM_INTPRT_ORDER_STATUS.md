# GNOM_INTPRT_ORDER_STATUS

> Information about which order contacts filed this interpretation.

**Primary key:** `GNOM_INTPRT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GNOM_INTPRT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the interpretation record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `FILED_BY_ORDER_ID` | NUMERIC |  | The ORD ID for which the results include this interpretation. |
| 5 | `ORD_DATE_REAL` | FLOAT |  | The ORD DAT for which the results include this interpretation |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GNOM_INTPRT_ID` | [GNOM_INTPRT_IDENT](GNOM_INTPRT_IDENT.md) | sole_pk | high |

