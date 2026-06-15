# HH_OASIS_SNAPSHOT_HX

> This table stores the types of changes made to the Outcome and Assessment Information Set (OASIS) data set.

**Primary key:** `OASIS_SET_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OASIS_SET_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the data set record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `OASIS_SNPSHT_CHNG_TYPE_C_NAME` | VARCHAR |  | Records whether a data set key-value pair was added, modified, or removed since the last time a snapshot was taken. |
| 6 | `CHANGE_KEY` | VARCHAR |  | The name of the key which uniquely identifies a data point in the data set. This is often the name of the XML node for a given value in an export file, but could vary depending on dataset |
| 7 | `CHANGE_VALUE` | VARCHAR |  | The new value of the associated data set key as of this snapshot contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OASIS_SET_ID` | [HH_OASIS_INFO](HH_OASIS_INFO.md) | sole_pk | high |

