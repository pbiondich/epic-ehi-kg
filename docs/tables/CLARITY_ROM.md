# CLARITY_ROM

> This table reflects the information in the Hospital Rooms (ROM) master file.

**Primary key:** `ROOM_CSN_ID`  
**Columns:** 2  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ROOM_CSN_ID` | NUMERIC | PK | The serial number for the room contact of the room record. This number is unique across all room contacts in the system. |
| 2 | `ROOM_NAME` | VARCHAR |  | The name of the room. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [CLARITY_ADT](CLARITY_ADT.md) | `ROOM_CSN_ID` | high |

