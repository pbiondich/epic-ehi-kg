# PAT_EDU_HNDT_PROG_TRACK

> Table to store all handout progress related infomation across contacts.

**Primary key:** `PED_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PED_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the education record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HANDOUT_LINK_KEY` | VARCHAR |  | The handout link key to find the handout and the corresponding progress infomation. |
| 4 | `HANDOUT_LINK` | VARCHAR |  | The patient handout URL. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PED_ID` | [CL_PAT_EDU_NS](CL_PAT_EDU_NS.md) | sole_pk | high |

