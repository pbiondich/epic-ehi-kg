# CYCLE_CRYO_EGG

> Information about the eggs that are cryopreserved in a particular fertility treatment cycle.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the cycle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CRYO_EGG_ID_NAME` | VARCHAR |  | The custom ID title for the egg. If not set, the ID is based on the line number. |
| 4 | `CRYO_EGG_DATE` | DATETIME |  | The date of cryopreservation for eggs. |
| 5 | `CRYO_EGG_DAY` | INTEGER |  | The number of days of culture for the egg prior to cryopreservation. |
| 6 | `CRYO_EMBRYO_STAGE_C_NAME` | VARCHAR | org | The cryopreserved egg's stage. |
| 7 | `CRYO_EMBRYO_GAMETE_SOURCE_C_NAME` | VARCHAR | org | The cryopreserved egg's source, such as autologous, partner, or donor. |
| 8 | `CRYO_EMBRYO_GAMETE_STATE_C_NAME` | VARCHAR | org | The cryopreserved egg's state at the beginning of the cycle, such as fresh or thawed. |
| 9 | `CRYO_EGG_DONOR` | VARCHAR |  | The cryopreserved egg's donor ID. |
| 10 | `CRYOEGG_MATURITY_C_NAME` | VARCHAR | org | The cryopreserved egg's maturity. |
| 11 | `CRYO_EGG_COMMENTS` | VARCHAR |  | Comment for the egg. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

