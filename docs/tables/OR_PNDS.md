# OR_PNDS

> This table contains OR management system Perioperative Nursing Data Set (PNDS) elements.

**Primary key:** `ELEMENT_ID`  
**Columns:** 3  
**Joined by:** 29 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ELEMENT_ID` | VARCHAR | PK | The unique internal ID of the Perioperative Nursing Data Set (PNDS) element record. |
| 2 | `ELEMENT_ID_ELEMENT_NAME` | VARCHAR |  | The name of the PNDS record. |
| 3 | `ELEMENT_NAME` | VARCHAR |  | The name of the PNDS record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (29)

| From | Column | Confidence |
|------|--------|------------|
| [SMRTDTA_ELEM_AIEXTRACTED](SMRTDTA_ELEM_AIEXTRACTED.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_AUTH](SMRTDTA_ELEM_AUTH.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_BEREAVE](SMRTDTA_ELEM_BEREAVE.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_CONCEPT](SMRTDTA_ELEM_CONCEPT.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_CUST_SERVICE](SMRTDTA_ELEM_CUST_SERVICE.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_DATA](SMRTDTA_ELEM_DATA.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_DATASET](SMRTDTA_ELEM_DATASET.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_DEFICIENCY](SMRTDTA_ELEM_DEFICIENCY.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_DOCUMENT](SMRTDTA_ELEM_DOCUMENT.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_DONOR](SMRTDTA_ELEM_DONOR.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_ENCOUNTER](SMRTDTA_ELEM_ENCOUNTER.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_EPISODE](SMRTDTA_ELEM_EPISODE.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_EPISODE_GRP](SMRTDTA_ELEM_EPISODE_GRP.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_FIN_ASST_CAS](SMRTDTA_ELEM_FIN_ASST_CAS.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_HISTORY](SMRTDTA_ELEM_HISTORY.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_INFERT_CYCLE](SMRTDTA_ELEM_INFERT_CYCLE.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_LAB_RESULT](SMRTDTA_ELEM_LAB_RESULT.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_NOTE](SMRTDTA_ELEM_NOTE.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_ORDER](SMRTDTA_ELEM_ORDER.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_ORGAN](SMRTDTA_ELEM_ORGAN.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_PATIENT](SMRTDTA_ELEM_PATIENT.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_PAT_ENTERED](SMRTDTA_ELEM_PAT_ENTERED.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_PROBLEM](SMRTDTA_ELEM_PROBLEM.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_REGISTRY](SMRTDTA_ELEM_REGISTRY.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_RESULT](SMRTDTA_ELEM_RESULT.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_RESULT_CNCT](SMRTDTA_ELEM_RESULT_CNCT.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_STAGE](SMRTDTA_ELEM_STAGE.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_SYNOPTIC](SMRTDTA_ELEM_SYNOPTIC.md) | `ELEMENT_ID` | high |
| [SMRTDTA_ELEM_WAITING_LST](SMRTDTA_ELEM_WAITING_LST.md) | `ELEMENT_ID` | high |

