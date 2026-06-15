# NAMES_STATIC

> The table holds extracted data from the Non-Patient Person Name (EAM) master file. These records store name information (first/last, academic suffix, etc) for static master files referencing people (User (EMP), Provider (SER), and so forth).

**Primary key:** `RECORD_ID`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID_RECORD_NAME` | VARCHAR |  | Internationally formatted non-patient name of the person. |
| 2 | `RECORD_NAME` | VARCHAR |  | Internationally formatted non-patient name of the person. |
| 3 | `LAST_NAME` | VARCHAR |  | Stores the person's last name. |
| 4 | `LAST_NAME_SPOUSE` | VARCHAR |  | Stores the part of the person's last name from their spouse. |
| 5 | `FIRST_NAME` | VARCHAR |  | Stores the person's first name. |
| 6 | `MIDDLE_NAME` | VARCHAR |  | Stores the person's middle name. |
| 7 | `LAST_NAME_PREFIX` | VARCHAR |  | Stores the person's last name prefix. |
| 8 | `PREFERRED_NAME` | VARCHAR |  | Stores the name the person prefers to be called. |
| 9 | `GIVEN_NAME_INITIALS` | VARCHAR |  | Stores the initials for the person's given name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

