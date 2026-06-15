# CL_PROV_PIN

> This table contains provider insurance filing information for contacts in the Provider PIN (PIN) master file.

**Primary key:** `PIN_ID`, `CONTACT_DATE_REAL`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PIN_ID_PROV_REF_NAME` | VARCHAR |  | The provider or referral source name. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | The contact date in internal format. |
| 3 | `PROV_REF_NAME` | VARCHAR |  | The provider or referral source name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

