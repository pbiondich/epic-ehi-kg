# PROB_LNKSRC_ORL

> This table contains problems from a patient's problem list along with linked surgical logs and surgical procedures suspected of causing the problems.

**Primary key:** `PROBLEM_LIST_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier for the problem record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `LNK_SRC_ORL_ID` | VARCHAR |  | The linked surgical logs suspected of causing the problem. |
| 6 | `LNK_SRC_PNL_NUM` | INTEGER |  | The linked surgical log panels containing surgical procedures suspected of causing the problem. |
| 7 | `LNK_SRC_ORP_ID` | VARCHAR |  | The linked surgical procedures suspected of causing the problem. |
| 8 | `LNK_SRC_ORP_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 9 | `LNK_SRC_OPE_ID` | NUMERIC |  | The procedure additional data records for the linked source surgical procedures suspected of causing the problem. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

