# TECH_COMPLETE_INFO

> This table stores tech complete information for imaging procedures.

**Primary key:** `ORDER_PROC_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TECH_COMPLETE_INST_LOC_DTTM` | DATETIME (Local) |  | This item calculates the instant that the user listed in I ORD 52674 marked the study as Tech Complete, local to the time zone of the user's client. |
| 4 | `TECH_COMPLETE_USER_ID` | VARCHAR |  | This item stores the users who have marked an imaging study as tech completed. |
| 5 | `TECH_COMPLETE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `TECH_COMPLETE_INST_UTC_DTTM` | DATETIME (UTC) |  | This item captures the date and time in the Universal Time Coordinated (UTC) format that the user listed in I ORD 52674 marked the study as Tech Complete. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

