# LANGUAGE

> This contains a list of languages and their properties, both spoken and written.

**Primary key:** `LANGUAGE_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LANGUAGE_ID` | NUMERIC | PK | The unique identifier (.1 item) for the language record. |
| 2 | `LANGUAGE_ID_LANGUAGE_NAME` | VARCHAR |  | The language name. If the language is written and uses more than one script to represent it, the name will contain the script in parentheses after the language name. |
| 3 | `LANGUAGE_NAME` | VARCHAR |  | The language name. If the language is written and uses more than one script to represent it, the name will contain the script in parentheses after the language name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [COMM_TRACE_INFO](COMM_TRACE_INFO.md) | `LANGUAGE_ID` | high |

