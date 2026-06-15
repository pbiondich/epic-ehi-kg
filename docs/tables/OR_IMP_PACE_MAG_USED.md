# OR_IMP_PACE_MAG_USED

> This table stores information related to the Pacemaker - Magnet Pacemaker - Magnet Used on Device (I IMP 56741) item.

**Primary key:** `IMPLANT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique identifier for the implant record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PACEMAKER_MAG_USE_C_NAME` | VARCHAR | org | This item is used to store information on whether a magnet can be used on the device to prevent inhibition by electrocautery. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

