# AP_SPECIMEN_DESC

> Lab Anatomic Pathology case specimen descriptions.

**Primary key:** `SPECIMEN_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The internal Specimen record ID. |
| 2 | `AP_SPEC_DESCR_ID_TEST_NAME` | VARCHAR |  | The name of the test record. |
| 3 | `AP_SPEC_DESCR_CMT` | VARCHAR |  | This item is used for a free text description of an anatomic pathology specimen. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

