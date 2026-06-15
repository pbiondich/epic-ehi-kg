# MEDICATION_NOTES

> This table contains medication note information that can be attached to the medication order from order entry or other medication-related activities.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The ID number of the order record containing the medication note |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MED_NOTE_ID` | VARCHAR |  | The unique ID number for this medication note. |
| 4 | `MED_NOTE_CSN` | NUMERIC |  | The unique contact serial number for the patient encounter when this note was created. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 5 | `MED_NOTE_USER_ID` | VARCHAR |  | The unique ID of the user who wrote the medication note. |
| 6 | `MED_NOTE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `MED_NOTE_INSTANT` | DATETIME (Local) |  | The date and time when the medication note was created |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

