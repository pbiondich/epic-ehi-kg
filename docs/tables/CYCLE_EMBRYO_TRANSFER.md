# CYCLE_EMBRYO_TRANSFER

> This table holds data for the specific embryos transferred during a cycle.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 18  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the cycle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EMBRYO_STAGE_C_NAME` | VARCHAR | org | Stores stage at transfer for a specific embryo. |
| 4 | `EMBRYO_GRADE_C_NAME` | VARCHAR | org | Stores grade at transfer for a specific embryo. |
| 5 | `EMBRYO_FERT_METHOD_C_NAME` | VARCHAR |  | Stores the embryo's fertilization type at a given transfer. |
| 6 | `EMBRYO_ASSISTED_HATCHING_YN` | VARCHAR |  | Stores whether this specific embryo had any hatching assistance. |
| 7 | `EGG_EMBRYO_GAMETE_SOURCE_C_NAME` | VARCHAR | org | Stores the source of the egg for a specific embryo. The source being the participant that the gamete came from (donor, partner, self, etc). |
| 8 | `SPERM_EMBRYO_GAMETE_SOURCE_C_NAME` | VARCHAR |  | Stores the sperm source for a specific embryo. The source being the participant that the gamete came from (donor, partner, etc). |
| 9 | `EGG_EMBRYO_GAMETE_STATE_C_NAME` | VARCHAR | org | Stores the state of the egg at the beginning of the cycle. |
| 10 | `SPERM_EMBRYO_GAMETE_STATE_C_NAME` | VARCHAR |  | Stores the state of the sperm at the beginning of the cycle. |
| 11 | `EMBRYO_COMMENTS` | VARCHAR |  | Stores the comments for a specific embryo at transfer. |
| 12 | `EMBRYO_TRANSFER_DAY` | INTEGER |  | Stores the transfer day of a specific embryo. |
| 13 | `EMBRYO_OVERRIDE` | VARCHAR |  | Stores an embryo ID that a user specified. If not set, an embryo ID based on the line number (such as "Embryo 1") is shown to the end user. |
| 14 | `EMBRYO_PGT_A_C_NAME` | VARCHAR | org | Stores the documentation for a specific embryo's PGT-A testing during an embryo transfer. |
| 15 | `EMBRYO_PGT_M_C_NAME` | VARCHAR | org | Stores the documentation for a specific embryo's PGT-M testing during an embryo transfer. |
| 16 | `EMBRYO_PGT_SR_C_NAME` | VARCHAR | org | Stores the documentation for a specific embryo's PGT-SR testing during an embryo transfer. |
| 17 | `SPECIFIC_EMBRYO_GAMETE_STATE_C_NAME` | VARCHAR |  | Stores the state of the embryo (thawed or fresh) at the beginning of the cycle. Thawed means the embryo was thawed as an embryo. Fresh means that either the egg and sperm are fresh, or they were thawed as gametes and then fertilized. |
| 18 | `EMBRYO_DONATED_YN` | VARCHAR |  | Stores whether the embryo was donated for an embryo transfer cycle. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

