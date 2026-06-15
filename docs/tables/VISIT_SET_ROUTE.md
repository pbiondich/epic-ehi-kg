# VISIT_SET_ROUTE

> The VISIT_SET_ROUTE table contains information about the route, or generic provider record, assigned to a specific visit set.

**Primary key:** `VISIT_SET_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VISIT_SET_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the visit set record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact. |
| 5 | `ROUTE_DISCIPLINE_KEY` | VARCHAR |  | A key that identifies a single instance of a single required provider of a certain discipline, in the form <LDS ID>^<COUNT> where LDS ID is a discipline record stored in VISIT_SET_DISCIPLINE__DISCIPLINE_DISC_TYPE_ID and COUNT is a number greater than 0 but less than or equal to the count stored in VISIT_SET_DISCIPLINE__DISCIPLINE_COUNT on the same line as the discipline ID. For example, if we require 2 providers of discipline 1001, and 1 provider of discipline 2002, possible values for this column are limitted to: 1001^1, 1001^2, and 2002^1. Associated with these discipline requirements are the providers with whom to schedule with in order to fulfill them, stored in ROUTE_RESOURCE_PROV_ID. |
| 6 | `ROUTE_RESOURCE_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VISIT_SET_ID` | [VISIT_SET](VISIT_SET.md) | sole_pk | high |

