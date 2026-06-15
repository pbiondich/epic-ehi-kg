# RX_IVENT_DOC

> The intervention documentation table contains one record for each intervention that has documentation associated with it, and the text of that documentation. Rich text is stored in database but it is extracted as plain text here. The primary key for the intervention type table is INTERVENTION_ID, LINE.

**Primary key:** `INTERVENTION_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INTERVENTION_ID` | NUMERIC | PK FK→ | Unique ID of intervention. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DOC_TEXT` | VARCHAR |  | Text of the intervention documentation. The text will be in plain text, that is, no formatting information besides blank lines and possibly extra spaces will appear in the text. This column will automatically be truncated at 4000 characters. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |

