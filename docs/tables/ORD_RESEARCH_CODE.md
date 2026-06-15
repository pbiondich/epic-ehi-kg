# ORD_RESEARCH_CODE

> This table contains information about research studies that an order is associated with. The table includes a column that links to the corresponding Research Study (RSH) record.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RESEARCH_CODE_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 4 | `RSH_CODE_COMMENT` | VARCHAR |  | Any comments associated with a linked Research Study record. A Research Study record stores information about research studies. This column is used in combination with the RESEARCH_CODE_ID column and stores any comments a user may have made regarding the link between the Order and the research study. |
| 5 | `RSH_CODE_FROM_C_NAME` | VARCHAR |  | This item stores where the research association in Research Study record ID came from. This is so that we can track where an association was made, to avoid potentially overwriting data from one valid source with another, such as overwriting Research Association Grid data with Order-Specific question data. |
| 6 | `ENROLL_ID` | NUMERIC | FK→ | The unique ID of the research study association that has been linked to this order. Linking an order to a research study association means the order is related to the execution of the research study. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

