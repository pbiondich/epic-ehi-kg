# SPEC_GENETIC_CONTRIBUTORS

> The person that an egg or sperm came from. For embryos, this table stores the egg and sperm sources used to create the embryo.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `GEN_CONTRIB_NONPAT_RECORD_ID` | NUMERIC |  | Non-patients who are genetic contributors to the specimen, i.e. have provided the sperm or egg. This will store external donors who don't have a chart in the system. |
| 4 | `PAT_ROLE_C_NAME` | VARCHAR |  | Stores whether the genetic contributor for a specimen is the oocyte or sperm contributor. |
| 5 | `GAMETE_SOURCE_C_NAME` | VARCHAR | org | The type of genetic contribution. This includes autologous, partner, anonymous donor, and directed donor. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

