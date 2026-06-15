# APPT_CSN_COUNTS

> This table contains the appointment contact serial numbers (CSNs) linked to an authorization as well as the counts used for each CSN.

**Primary key:** `AUTH_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_ID` | NUMERIC | PK FK→ | The authorization ID for the authorization record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LINKED_APPT_CSNS` | NUMERIC |  | The contact serial numbers (CSNs) of all the appointments which fall within the dates on the authorization record. |
| 4 | `LINKED_APPT_COUNTS` | INTEGER |  | The used counts corresponding to a particular contact serial number (CSN) in the LINKED_APPT_CSN column linked to an Authorization record. |
| 5 | `USR_OVR_VST_COUNT_YN` | VARCHAR |  | Flag to say user has overridden the visit counts. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_ID` | [AUTHORIZATIONS](AUTHORIZATIONS.md) | overflow_master | medium |

