# HH_CNTCT_INFO

> This table contains the Home Health Contact Type noadd single items. These items do not change when a new contact is created for the Home Health Contact Type record.

**Primary key:** `CONTACT_TYPE_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONTACT_TYPE_ID_CONTACT_TYPE_NAME` | VARCHAR |  | Home Health Contact Type name |
| 2 | `CONTACT_TYPE_NAME` | VARCHAR |  | Home Health Contact Type name |
| 3 | `HH_ENC_CLASS_C_NAME` | VARCHAR |  | The calculated encounter class of a contact type. |
| 4 | `PREADMIT_VISIT_YN` | VARCHAR |  | Whether a given visit is considered a home health preadmission visit preceding the creation of a certification period. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

