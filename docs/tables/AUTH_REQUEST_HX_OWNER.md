# AUTH_REQUEST_HX_OWNER

> The AUTH_REQUEST_HX_OWNER table contains the history of review owners assigned to authorization requests. These assignments include user and the UM role associated with the user's UM security class at the time of assignment.

**Primary key:** `AUTH_REQUEST_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_REQUEST_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the authorization request record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `OWNER_USER_EMP_USER_ID` | VARCHAR |  | The user assigned as a review owner to an auth request |
| 5 | `OWNER_USER_EMP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `OWNER_UM_ROLE_C_NAME` | VARCHAR |  | The role of a review owner assigned to an auth request |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_REQUEST_ID` | [AUTH_REQUEST](AUTH_REQUEST.md) | sole_pk | high |

