# ADVICE_TEXT

> This table extracts the text that was offered as care advice.

**Primary key:** `CA_ID`, `VERSION_DATE_REAL`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CA_ID_CARE_ADVICE_NAME` | VARCHAR |  | The name of the care advice record. |
| 2 | `VERSION_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this version in your system. The integer portion of the number specifies the date of the version. The digits after the decimal point indicate multiple versions on one day. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CA_TEXT` | VARCHAR |  | The text of the Care Advice given to a patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

