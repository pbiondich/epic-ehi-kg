# V_EHI_SDD_ENTRY_INTERPRETATION

> This view converts the ENTRY_INTERPRETATION column in SDD_ENTRIES into an external-facing format for EHI Export. This table should be used in tandem with SDD_ENTRIES, using the SDOH_DATA_ID, CONTACT_DATE_REAL, and LINE columns to join the data together.

**Primary key:** `SDOH_DATA_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SDOH_DATA_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the social driver data record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `ENTRY_INTERPRETATION_EXTERNAL` | VARCHAR |  | Stores the interpretation this entry is reporting. This might be the output of a scoring rule or some other scoring value. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SDOH_DATA_ID` | [SDD_DATA](SDD_DATA.md) | sole_pk | high |

