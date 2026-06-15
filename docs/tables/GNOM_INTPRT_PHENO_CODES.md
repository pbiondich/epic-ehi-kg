# GNOM_INTPRT_PHENO_CODES

> Codes for the phenotype that defines the context of this interpretation.

**Primary key:** `GNOM_INTPRT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GNOM_INTPRT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the interpretation record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `PHENOTYPE_SYSTEM_C_NAME` | VARCHAR |  | Select the coding system used to define the associated phenotype in I GNI 1902. |
| 5 | `PHENOTYPE_CODE` | VARCHAR |  | The phenotype code associated with the genomic interpretation. |
| 6 | `PHENOTYPE_NAME` | VARCHAR |  | Enter the name of the phenotype specified in I GNI 1902, as defined by the coding system specified in I GNI 1901. An example of phenotype name is "Acyl-CoA dehydrogenase family, member 9, deficiency of" for MedGen-Dis C1970173. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GNOM_INTPRT_ID` | [GNOM_INTPRT_IDENT](GNOM_INTPRT_IDENT.md) | sole_pk | high |

