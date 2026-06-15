# SERVICE_PLAN_VISIT_SET

> The SERVICE_PLAN_VISIT_SET table contains visit sets for each version of the service plan that each describe a single recurring visit required to address specific elements of care required for a patient. A row represents a visit set included in a service plan version.

**Primary key:** `SERVICE_PLAN_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SERVICE_PLAN_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the service plan record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact. |
| 5 | `VISIT_SET_ID` | NUMERIC | FK→ | The visit sets that make up this version of the service plan. |
| 6 | `VISIT_SET_CSN_ID` | NUMERIC |  | The versions of the visit sets that make up this version of the service plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SERVICE_PLAN_ID` | [SERVICE_PLAN](SERVICE_PLAN.md) | sole_pk | high |
| `VISIT_SET_ID` | [VISIT_SET](VISIT_SET.md) | sole_pk | high |

