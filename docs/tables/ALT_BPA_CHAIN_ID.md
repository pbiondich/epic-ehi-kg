# ALT_BPA_CHAIN_ID

> This table holds the asynchronous OurPractice Advisory (OPA) chains that are associated with this Alert's (ALT) contact.

**Primary key:** `ALERT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALERT_ID` | NUMERIC | PK shared | The ALT record ID |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The Line Count |
| 4 | `ALT_CHAIN_ID` | NUMERIC |  | This item links alert record contacts that occur in a chain together with a unified ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

