# RAD_THERAPY_ASSOC_COURSES

> Lists external radiation courses linked to an episode. Each row is a reference to a course of radiation treatment that was documented in an external system such as MOSAIQ or ARIA. If the course was automatically associated with a radiation-therapy episode when the course was interfaced to Epic, the likelihood of the match ("match score") is indicated as well.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID of the episode of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RAD_THERAPY_COURSE_SRC_SYS_C_NAME` | VARCHAR |  | This item is for episodes associated with courses of radiation documented in third-party software systems (radiation-therapy episodes). The source system is specified in this item, and the ID of the course is specified in the counterpart Radiation Therapy Course ID (I HSB 38805). |
| 4 | `RAD_THERAPY_COURSE_IDENT` | VARCHAR |  | This item is for episodes associated with courses of radiation documented in third-party software systems (radiation-therapy episodes). The ID of the course is specified in this item, and the source system is specified in the counterpart Radiation Therapy Course Source System (I HSB 38800). |
| 5 | `RAD_THERAPY_COURSE_MATCH_SCORE` | INTEGER |  | This item is for episodes associated with courses of radiation documented in third-party software systems (radiation-therapy episodes). This item records the match score for a course that is automatically linked to the episode by the system. (The course in question is identified by related items Radiation Therapy Course Source System (I HSB 38800) and Radiation Therapy Course ID (I HSB 38805) combined.) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

