# SDD_DATA

> This table stores defining information about a patient's SDOH data. Each row in this table represents documentation for a single SDOH domain for a single patient.

**Primary key:** `SDOH_DATA_ID`  
**Columns:** 5  
**Org-specific columns:** 1  
**Joined by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SDOH_DATA_ID` | NUMERIC | PK | The unique identifier (.1 item) for the social driver data record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Stores the record status. SDD only supports soft deleted records. |
| 3 | `DOMAIN_C_NAME` | VARCHAR | org | Stores the domain this record stores data for. |
| 4 | `PAT_ID` | VARCHAR | FK→ | The patient this SDD record stores data for. |
| 5 | `CONCERNS_PRESENT_YN` | VARCHAR |  | Tracks whether the patient has needs in any source for this domain. Checks the most recent entry across all sources to determine if there is a concern. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (5)

| From | Column | Confidence |
|------|--------|------------|
| [SDD_ENTRIES](SDD_ENTRIES.md) | `SDOH_DATA_ID` | high |
| [SDD_ORDERS](SDD_ORDERS.md) | `SDOH_DATA_ID` | high |
| [SDD_PROBLEMS](SDD_PROBLEMS.md) | `SDOH_DATA_ID` | high |
| [SDD_WANTS_ASSISTANCE](SDD_WANTS_ASSISTANCE.md) | `SDOH_DATA_ID` | high |
| [V_EHI_SDD_ENTRY_INTERPRETATION](V_EHI_SDD_ENTRY_INTERPRETATION.md) | `SDOH_DATA_ID` | high |

