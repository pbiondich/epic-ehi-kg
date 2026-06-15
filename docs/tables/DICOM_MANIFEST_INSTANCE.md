# DICOM_MANIFEST_INSTANCE

> This table contains a manifest's instance level metadata.

**Primary key:** `MANIFEST_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MANIFEST_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the subject name record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `UID_IDENT` | VARCHAR |  | The DICOM SOP instance UID (attribute 0008,0018). |
| 5 | `SOP_CLASS_C_NAME` | VARCHAR |  | The SOP Class UID of this Instance (attribute 0008,0016). |
| 6 | `BELONGS_TO_SERIES` | VARCHAR |  | The Series UID of the series this instance belongs to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MANIFEST_ID` | [DICOM_MANIFEST](DICOM_MANIFEST.md) | sole_pk | high |

