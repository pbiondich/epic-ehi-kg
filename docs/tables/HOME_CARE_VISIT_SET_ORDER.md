# HOME_CARE_VISIT_SET_ORDER

> Home care visit set Information. This table contains home care order (LVO) specific information for visit sets.

**Primary key:** `VISIT_SET_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VISIT_SET_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the visit set record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `VERBAL_ORDER_ID` | VARCHAR | FK→ | Stores the home care order (LVO) ID for the visit set. |
| 6 | `VERBAL_ORDER_SUPPRESS_C_NAME` | VARCHAR |  | This stores whether a user decided to not create an order for the visit set or the visit set was discontinued upon discipline discharge. |
| 7 | `VISIT_AUTH_STATUS_C_NAME` | VARCHAR |  | Auth status for the visit set |
| 8 | `ACTION_VISIT_LVO_C_NAME` | VARCHAR |  | The action taken on the visit set which led to the creation of the order. |
| 9 | `PRIOR_DISCON_DATE` | DATETIME |  | The prior discontinue date of the visit set for the corresponding visit set version at a particular time. |
| 10 | `PRIOR_ORDER_NOTE_CSN_ID` | NUMERIC |  | The prior order comment CSN of the visit set for the corresponding visit set version at a particular time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VERBAL_ORDER_ID` | [HH_VO_INFO](HH_VO_INFO.md) | sole_pk | high |
| `VISIT_SET_ID` | [VISIT_SET](VISIT_SET.md) | sole_pk | high |

