# GNOM_INTPRT_VER_INFO

> Main table for information in a single version of a genomic interpretation.

**Primary key:** `GNOM_INTPRT_ID`, `CONTACT_DATE_REAL`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GNOM_INTPRT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the interpretation record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `GNOM_INTPRT_ENTRY_SRC_C_NAME` | VARCHAR |  | The method that was used to create the interpretation. |
| 4 | `EXTERNAL_YN` | VARCHAR |  | Indicates whether the interpretation should be considered external, such as auto-reconciliation by Happy Together using data from an external organization. |
| 5 | `FILED_BY_RESULT_ID` | VARCHAR |  | The OVR ID for which the results include this interpretation. |
| 6 | `GNOM_INTPRT_CLASS_C_NAME` | VARCHAR |  | The classification with respect to this particular phenotype and mode of inheritance. For germline variants, category values Pathogenic, Likely pathogenic, Uncertain Significance, Likely benign, and Benign correspond to values in LOINC 53037-8. For somatic variants found during tumor testing, category values Tier 1: Strong significance, Tier 2: Potential Significance, Tier 3: Unknown clinical significance, and Tier 4: Benign or likely benign correspond to values in the ACMG Tier System for significance of somatic variants. For pharmacogenomic variants, use value 300-Drug response. For repeat expansion variants, category values Complete Penetrance, Incomplete Penetrance, Uncertain Penetrance, Premutation, Intermediate, Mutable Normal Allele, Recessive Allele, and Normal Allele correspond to repeat expansion guidelines. |
| 7 | `MODE_OF_INHERITANCE_C_NAME` | VARCHAR |  | Enter the mode of inheritance for the phenotype. |
| 8 | `PENETRANCE` | NUMERIC |  | Enter the penetrance of the phenotype for this variant. This should be a value between 0.0 and 1.0. Penetrance is defined as the percentage of individuals with a given genotype who exhibit the phenotype associated with that genotype. |
| 9 | `PHENOTYPE_DESCRIPTION` | VARCHAR |  | Enter a free-text description of the specified phenotype. |
| 10 | `NARR_NOTE_CSN_ID` | NUMERIC |  | A free-text description of the interpretation and the clinical implication for the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GNOM_INTPRT_ID` | [GNOM_INTPRT_IDENT](GNOM_INTPRT_IDENT.md) | sole_pk | high |

