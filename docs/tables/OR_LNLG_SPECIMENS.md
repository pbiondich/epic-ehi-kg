# OR_LNLG_SPECIMENS

> This table contains the Specimens information for the surgical log.

**Primary key:** `RECORD_ID`  
**Columns:** 6  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `SPECIMEN_ID` | VARCHAR | shared | The ID of the specimen. |
| 3 | `SPEC_SENT_TO_C_NAME` | VARCHAR | org | The location to which the specimen was sent. |
| 4 | `SPECIMEN_SITE_C_NAME` | VARCHAR | org | The site the specimen was collected from. |
| 5 | `SPECIMEN_DATE_SENT` | DATETIME |  | The date the specimen was sent. |
| 6 | `SPECIMEN_TIME_SENT` | DATETIME (Local) |  | The time the specimen was sent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

