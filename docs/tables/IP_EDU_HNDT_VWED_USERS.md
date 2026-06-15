# IP_EDU_HNDT_VWED_USERS

> Stores the WPR IDs of all MyChart users that have viewed the patient handout for current contact.

**Primary key:** `PED_ID`, `CONTACT_DATE_REAL`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PED_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the education record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this contact. |
| 4 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this contact. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `HANDOUT_VIEWED_USRS_MYPT_ID` | VARCHAR |  | Stores the WPR IDs of all MyChart users that have viewed the patient handout for current contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PED_ID` | [CL_PAT_EDU_NS](CL_PAT_EDU_NS.md) | sole_pk | high |

