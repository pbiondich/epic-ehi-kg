# IP_LINKED_CSN

> This table displays the Contact Serial Numbers (CSNs) for linked contacts.

**Primary key:** `INPATIENT_DATA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique identifier for the inpatient record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LINKED_CSN` | VARCHAR |  | The Contact Serial Number (CSN) of the linked contact. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 4 | `CONTACT_INSTANT_TM` | DATETIME (Local) |  | This column will store the instant for the linked contact. Instant stored here will be used by One Time documentation flowsheets. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

