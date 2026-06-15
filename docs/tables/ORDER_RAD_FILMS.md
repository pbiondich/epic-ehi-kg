# ORDER_RAD_FILMS

> ORDER_RAD_FILMS stores information entered about the number & size of films used when a radiology order is performed.

**Primary key:** `ORDER_PROC_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line count for this table as determined by the number of films used/film size combinations entered. |
| 3 | `FILMS_USED` | INTEGER |  | The number of films used (of the size FILM_SIZE_C). |
| 4 | `FILM_SIZE_MR_C_NAME` | VARCHAR | org | The size of films category ID for films used (FILMS_USED). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

