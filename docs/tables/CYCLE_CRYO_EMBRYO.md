# CYCLE_CRYO_EMBRYO

> Embryos that were cryopreserved during a specific fertility treatment cycle.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 19  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the cycle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CRYO_EMBRYO_ID_NAME` | VARCHAR |  | A custom ID title for the cryopreservation. If not set, users will see a generated ID based on the line number, such as "Embryo N." |
| 4 | `CRYO_EMBRYO_DATE` | DATETIME |  | The date that the embryos were cryopreserved. |
| 5 | `CRYO_EMBRYO_DAY` | INTEGER |  | The number of days that an embryo has been in culture when it is cryopreserved. |
| 6 | `CRYO_EMBRYO_STAGE_C_NAME` | VARCHAR | org | The embryo's stage when it's cryopreserved. |
| 7 | `CRYO_EMBRYO_GRADE_C_NAME` | VARCHAR | org | The embryo's grade at cryopreservation. |
| 8 | `CRYO_EMBRYO_FERT_METHOD_C_NAME` | VARCHAR |  | The fertilization method (e.g. conventional IVF or ICSI) used for the embryo. |
| 9 | `CRYO_EMBRYO_PGT_A_C_NAME` | VARCHAR | org | The cryopreserved embryo's PGT-A result. |
| 10 | `CRYO_EMBRYO_PGT_M_C_NAME` | VARCHAR | org | The cryopreserved embryo's PGT-M result. |
| 11 | `CRYO_EMBRYO_PGT_SR_C_NAME` | VARCHAR | org | The cryopreserved embryo's PGT-SR result. |
| 12 | `CRYO_EMBRYO_AH_YN` | VARCHAR |  | Whether assisted hatching was performed on the cryopreserved embryo. |
| 13 | `EGG_EMBRYO_GAMETE_SOURCE_C_NAME` | VARCHAR | org | The cryopreserved embryo's egg source, such as if it was autologous or came from a partner or donor. |
| 14 | `SPERM_EMBRYO_GAMETE_SOURCE_C_NAME` | VARCHAR |  | The cryopreserved embryo's sperm source, such as a partner or donor. |
| 15 | `EGG_EMBRYO_GAMETE_STATE_C_NAME` | VARCHAR | org | The cryopreserved embryo's egg state (fresh or thawed) at the beginning of the treatment cycle. |
| 16 | `SPERM_EMBRYO_GAMETE_STATE_C_NAME` | VARCHAR |  | The cryopreserved embryo's sperm state (fresh or thawed) at the start of the cycle. |
| 17 | `CRYO_EMBRYO_EGG_DONOR` | VARCHAR |  | The cryopreserved embryo's egg donor ID. |
| 18 | `CRYO_EMBRYO_SPERM_DONOR` | VARCHAR |  | The cryopreserved embryo's semen donor ID. |
| 19 | `CRYO_EMBRYO_COMMENTS` | VARCHAR |  | Comment for an embryo being cryopreserved. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

