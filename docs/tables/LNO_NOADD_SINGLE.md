# LNO_NOADD_SINGLE

> The LNO_NOADD_SINGLE table contains information about your patient note records. This includes patient summary extracts, lab result reports, and other generated patient documents. All LNO records are included in this table.

**Primary key:** `EXTRACT_ID`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EXTRACT_ID` | NUMERIC | PK | The unique ID of the patient summary extract record. |
| 2 | `EXTRACT_NAME` | VARCHAR |  | The internal name of the patient summary extract. |
| 3 | `TRANSFER_DATE` | DATETIME |  | The date that the extract was transferred to the external document management system. |
| 4 | `EXT_DOC_LINK` | VARCHAR |  | The link to the document stored in an external document management system. |
| 5 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 6 | `EXTRACT_INSTANT` | DATETIME (Local) |  | The instant in which the patient summary extract was created. |
| 7 | `TRIGGER_USER_ID` | VARCHAR |  | The user who triggered the extract. Contains the internal ID of that user. |
| 8 | `TRIGGER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

