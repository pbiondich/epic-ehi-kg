# AP_SPEC_ATTRIBUTE

> Lab Anatomic Pathology Specimen Attributes.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AP_SPEC_ATTR_C_NAME` | VARCHAR | org | The specimen attribute category number for the anatomic pathology specimen. |
| 4 | `AP_ATTR_DTTM_DTTM` | DATETIME (UTC) |  | The instant when an attribute is applied to an anatomic pathology specimen. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

