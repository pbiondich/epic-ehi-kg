# NCDR_EPDIV3_DEMOGRAPHICS

> This table contains information from the Demographics section of the NCDR EP Device registry v3.0.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The associated patient's EPT .1 |
| 3 | `CUR_UNOS_STAGE_C_NAME` | VARCHAR | org | The current state of the registry record |
| 4 | `REG_OVRIDE_CONTEXT` | VARCHAR |  | Stores the override context string to identify the correct override record for the registry settings record (HFR) |
| 5 | `RACE_MIDL_EASTERN_N_AFRICAN_YN` | VARCHAR |  | Indicates if the patient is Middle Eastern or North African as determined by the patient/family. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

