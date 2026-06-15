# ORDER_RAD_ADDEND

> This table stores information about imaging addenda.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADDENDUM_STATUS_C_NAME` | VARCHAR |  | The addendum status category ID for the order |
| 4 | `ADDEND_RAD_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `ADDENDED_DT` | DATETIME |  | The date the addendum was signed. |
| 6 | `ADDENDED_TM` | DATETIME (Local) |  | The time the addendum was signed. |
| 7 | `ADDENDED_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant an addendum was created, in UTC time zone. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

