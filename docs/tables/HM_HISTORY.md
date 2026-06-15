# HM_HISTORY

> The HM_HISTORY table records information about completed and manually overridden clinical system health maintenance topics that apply to each patient. This information is found in your system by the following path: clinical system Supervisor Menu > Supervisor's menu > Patient Health Maint option, or by clicking the clinical system client Health Maintenance button.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting’s encryption utility. |
| 2 | `LINE` | INTEGER | PK | Identifies the health maintenance topic within the patient’s record. |
| 3 | `HM_COMP_TYPE_C_NAME` | VARCHAR |  | Stores the type of Health Maintenance completion |
| 4 | `HM_COMP_UTC_DTTM` | DATETIME (UTC) |  | Instant of Health Maintenance completion. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

