# NAMES

> The table extracts data from the Person Name (EAN) master file. These records store name information (first/last, academic suffix, etc).

**Primary key:** `RECORD_ID`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The is the internal ID of the record |
| 2 | `RECORD_NAME` | VARCHAR |  | This is the name of the record |
| 3 | `LAST_NAME` | VARCHAR |  | Stores the person's last name. |
| 4 | `LAST_NAME_SPOUSE` | VARCHAR |  | Stores the part of the person's last name from their spouse. |
| 5 | `FIRST_NAME` | VARCHAR |  | Stores the person's first name. |
| 6 | `MIDDLE_NAME` | VARCHAR |  | Stores the person's middle name. |
| 7 | `LAST_NAME_PREFIX` | VARCHAR |  | Stores the person's last name prefix. |
| 8 | `PREFERRED_NAME` | VARCHAR |  | Stores the name the person prefers to be called. |
| 9 | `GIVEN_NAME_INITIALS` | VARCHAR |  | The initials for the person's given names. |
| 10 | `FATHER_NAME` | VARCHAR |  | Stores the person's father's name. |
| 11 | `GRANDFATHER_NAME` | VARCHAR |  | Stores the person's grandfather's name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

