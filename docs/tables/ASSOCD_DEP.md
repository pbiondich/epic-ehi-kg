# ASSOCD_DEP

> This table contains information about the location (department, room, and bed) associated with an Infection Control abstraction.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ASSOCD_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 4 | `ASSOCD_ROM_ID_ROOM_NAME` | VARCHAR |  | The name of the Room record. |
| 5 | `ASSOCD_BED_ID` | VARCHAR |  | The unique ID of the bed record (BED .1) associated with the infection case. |
| 6 | `ASSOCD_BED_ID_BED_LABEL` | VARCHAR |  | The name of the bed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

