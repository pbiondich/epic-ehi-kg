# OR_WARMING_DEVICE_DETAILS

> This table stores details about the application of a warming device.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `APPLICATION_START_TM` | DATETIME (Local) |  | This column stores when the warming device setting was applied. |
| 4 | `APPLICATION_TEMPERATURE` | NUMERIC |  | This column stores the temperature setting for the warming device. |
| 5 | `APPLICATION_PRESSURE` | NUMERIC |  | This column stores the pressure setting for the warming device. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

