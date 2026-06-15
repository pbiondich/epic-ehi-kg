# ORD_PROVISIONAL_VERIFY

> Holds items for provisional verify.

**Primary key:** `ORDER_MED_ID`, `CONTACT_DATE_REAL`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `TRAINEE_VER_YN` | VARCHAR |  | Flag indicating an order was provisionally verified by a trainee |
| 5 | `MED_PROV_COMMENT` | VARCHAR |  | Trainee pharmacist comments added to an order during provisional verify. |
| 6 | `TRAINEE_VERIFY_DTTM` | DATETIME (UTC) |  | Stores the UTC date and time of when an order was provisionally verified by a trainee. |
| 7 | `WAS_PROV_REVERTED_YN` | VARCHAR |  | Indicates that provisional verify changes were reverted before the order was fully verified |
| 8 | `TRAINEE_VERIFY_LOCAL_DTTM` | DATETIME (Local) |  | Stores the local date and time of when an order was provisionally verified by a trainee. |
| 9 | `TRAINEE_REJECTED_YN` | VARCHAR |  | Flag indicating an order was provisionally rejected by a trainee |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

