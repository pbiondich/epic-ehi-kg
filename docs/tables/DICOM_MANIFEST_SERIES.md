# DICOM_MANIFEST_SERIES

> This table contains a manifest's series level metadata.

**Primary key:** `MANIFEST_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MANIFEST_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the subject name record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `UID_IDENT` | VARCHAR |  | The Series Instance UID for this imaging series (attribute 0020,000E). |
| 5 | `MODALITY_C_NAME` | VARCHAR |  | The DICOM Series modality type (attribute 0008,0060). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MANIFEST_ID` | [DICOM_MANIFEST](DICOM_MANIFEST.md) | sole_pk | high |

