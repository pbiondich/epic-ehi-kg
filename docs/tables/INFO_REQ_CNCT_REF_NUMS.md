# INFO_REQ_CNCT_REF_NUMS

> This table contains information about Reference Numbers on Additional Information Contacts.

**Primary key:** `INFO_REQ_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INFO_REQ_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the Additional Information Request record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `REFERENCE_NUM` | VARCHAR |  | Stores an identifier to uniquely identify this Additional Information Contact in this system. |
| 5 | `REF_NUM_TYPE_C_NAME` | VARCHAR |  | Denotes the type of identifier used to identify this Additional Information Contact in this system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INFO_REQ_ID` | [INFO_REQUEST](INFO_REQUEST.md) | sole_pk | high |

