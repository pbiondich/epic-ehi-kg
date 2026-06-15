# VARIANT

> Main variant result table.

**Primary key:** `VARIANT_ID`  
**Columns:** 80  
**Joined by:** 18 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VARIANT_ID` | NUMERIC | PK | The unique identifier for the variant record. |
| 2 | `VARIANT_TYPE_C_NAME` | VARCHAR |  | The type of variation category ID for the variant. |
| 3 | `VARIANT_NAME` | VARCHAR |  | The name assigned to the variant. |
| 4 | `HGVS_NAME` | VARCHAR |  | The HGVS name assigned to the variant. |
| 5 | `GENOME_ASSEMBLY_C_NAME` | VARCHAR |  | The category ID corresponding to the reference assembly used for analyzing this variant. |
| 6 | `CHROMOSOME_C_NAME` | VARCHAR |  | The category ID corresponding to the chromosome the variant is found on. |
| 7 | `START_POSITION` | INTEGER |  | The position where the variation starts. |
| 8 | `STOP_POSITION` | INTEGER |  | The position where the variation ends. |
| 9 | `DNA_REGION` | VARCHAR |  | The region of a chromosome or gene where the variant is located. For example, this could be an exon, intron, regulatory region, or a functional domain. |
| 10 | `GENE_C_NAME` | VARCHAR |  | The category ID corresponding to the gene name. |
| 11 | `GENE` | VARCHAR |  | The gene name. This column will be deprecated in the February 2027 release. It is being replaced by column REPORTED_GENE_NAME in table VARIANT_GENES. |
| 12 | `GENE_SYSTEM_C_NAME` | VARCHAR |  | The category ID corresponding to the source that defined the gene name. |
| 13 | `TRANSCRIPT_REF_SEQ` | VARCHAR |  | The external identifier defining the Transcript Reference Sequence. |
| 14 | `TRANSCRIPT_SYSTEM_C_NAME` | VARCHAR |  | The category ID for the source that defined the Transcript Reference Sequence. |
| 15 | `DNA_CHANGE` | VARCHAR |  | The change at the DNA level relative to the Transcript Reference Sequence. |
| 16 | `DNA_VAR_TYPE_C_NAME` | VARCHAR |  | The category ID corresponding to the DNA sequence variation type. |
| 17 | `AMINO_ACID_CHANGE` | VARCHAR |  | The change at the amino acid (protein) level caused by the DNA change. |
| 18 | `PROTEIN_REF_SEQ` | VARCHAR |  | The external identifier defining the Protein Reference Sequence. |
| 19 | `GENOMIC_REF_SEQ` | VARCHAR |  | The external ID defining the Genomic Reference Sequence. |
| 20 | `GEN_SEQ_SYSTEM_C_NAME` | VARCHAR |  | The category ID for the source that defined the Genomic Reference Sequence. |
| 21 | `REFERENCE_ALLELE` | VARCHAR |  | The DNA string in the reference sequence (Ref Allele) with which the DNA string in the test sample differs. |
| 22 | `OBSERVED_ALLELE` | VARCHAR |  | The DNA sequence in the test sample (Ref Allele) that is different from the DNA sequence in the reference sequence (Ref Allele). |
| 23 | `GENOMIC_DNA_CHANGE` | VARCHAR |  | The change at the DNA level relative to the Genomic Reference Sequence. |
| 24 | `ALLELIC_STATE_C_NAME` | VARCHAR |  | The allelic state category ID for the variant. |
| 25 | `ALLELIC_FREQUENCY` | NUMERIC |  | Reports the percentage of all of the reads at this genomic location that were represented by the given allele. For homozygotes it will be close to 100%; for heterozygotes it will be close to 50%. It can be a smaller number when there are mosaics or multiple chromosomes, or mixtures of tumor cells and normal cells. It is stored in the system as a decimal between 0 and 1 - this is calculated by dividing the percentage by 100. This field displays to end users as Variant Allele Fraction. |
| 26 | `CYTOGENETIC_LOC` | VARCHAR |  | The cytogenetic location of the variant. |
| 27 | `ALLELIC_READ_DEPTH` | INTEGER |  | The read depth (or coverage) for the variant. |
| 28 | `PENETRANCE` | NUMERIC |  | The penetrance for the variant. |
| 29 | `GENOMIC_SOURCE_C_NAME` | VARCHAR |  | The category ID corresponding to the source of the tissue for this variant. |
| 30 | `METHOD_TYPE_C_NAME` | VARCHAR |  | The category ID for the type of method used to determine this variant. |
| 31 | `ALLELIC_PHASE_C_NAME` | VARCHAR |  | The category ID that defines the parental set(s) of chromosomes a variant was inherited from, if any. If it was not inherited from the tested parent(s) then the category IDs of "De novo", "Not Maternal", or "Not Paternal" are used as appropriate. This field displays to end users as Parental Inheritance. |
| 32 | `ALLELIC_BASIS_C_NAME` | VARCHAR |  | The category ID corresponding to the evidence on which the allelic phase (which displays to end users as parental inheritance) was concluded. This field displays to end users as Basis For Parental Inheritance. |
| 33 | `BOUNDARY_PRECISION` | VARCHAR |  | Structural variant narrative description of the boundary precision. |
| 34 | `REPORTED_ACGH_RATIO` | NUMERIC |  | Structural variant reported aCGH Ratio. |
| 35 | `ALLELE_LENGTH` | INTEGER |  | Structural variant allele length. |
| 36 | `INNER_START` | INTEGER |  | Structural variant inner start position. |
| 37 | `INNER_END` | INTEGER |  | Structural variant inner end position. |
| 38 | `OUTER_START` | INTEGER |  | Structural variant outer start position. |
| 39 | `OUTER_END` | INTEGER |  | Structural variant outer end position. |
| 40 | `COPY_NUMBER` | INTEGER |  | Genomic structural variant copy number as an integer. To prepare for the future deprecation of this column, your content should use either the COPY_NUMBER_LOWER or the COPY_NUMBER_UPPER columns or both. |
| 41 | `ASSESSMENT_C_NAME` | VARCHAR |  | The category ID corresponding to the value in LOINC 69548-6, indicating whether the variant is present, absent, indeterminate, or if no call was made. |
| 42 | `CLINICAL_SIGNIF_C_NAME` | VARCHAR |  | The category ID corresponding to the variant's classification. The name of this item was changed from clinical significance to variant classification. It appears as variant classification in end-user facing locations, but the column name remains CLINICAL_SIGNIF_C for backwards compatibility. |
| 43 | `GENOTYPE` | VARCHAR |  | Genotype Name, used in combination with the column GENE (VAR 1210) to describe a Pharmacogenomic Variant. |
| 44 | `PGX_DRUG_METAB_C_NAME` | VARCHAR |  | Stores effect on drug metabolism for a pharmacogenomic variant. |
| 45 | `PGX_DRUG_EFFICACY_C_NAME` | VARCHAR |  | Predicted phenotype for ability of drug to bind to intended site in order to deliver intended effect. |
| 46 | `PGX_HIGH_RISK_C_NAME` | VARCHAR |  | Predicted phenotype for risk of adverse drug reaction. |
| 47 | `VARIANT_FUNC_EFFECT_C_NAME` | VARCHAR |  | The category ID for the functional effect of the variant |
| 48 | `VARIANT_MOLEC_CONSEQ_C_NAME` | VARCHAR |  | The molecular consequence category ID for the variant. |
| 49 | `MOSAICISM_C_NAME` | VARCHAR |  | The mosaicism category ID for the variant record as reported by the lab. |
| 50 | `FRACTIONAL_COPY_NUMBER` | NUMERIC |  | Genomic structural variant copy number with two decimal places of precision. To prepare for the future deprecation of this column, your content should use either the COPY_NUMBER_LOWER or the COPY_NUMBER_UPPER columns or both. |
| 51 | `IS_AMPLIFICATION_YN` | VARCHAR |  | Indicates whether the copy number variation meets the amplification threshold for this variant. 'Y' indicates that the variant has met the threshold. 'N' indicates that the variant is known to not meet the threshold. NULL might indicate that amplification does not apply, was not resulted, or could not be determined. |
| 52 | `GENE_ID` | NUMERIC | FK→ | Gene where the variant is located. This column will be deprecated in the February 2027 release. It is being replaced by column GENE_ID in table VARIANT_GENES. |
| 53 | `GENE_ID_RECORD_SYMBOL` | VARCHAR |  | The current symbol for this gene. In cases of disagreement, the current HGNC symbol will be used. |
| 54 | `IS_EXTERNAL_YN` | VARCHAR |  | Indicates whether the variant should be considered external, such as auto-reconciliation by Happy Together using data from an external organization. |
| 55 | `PERSISTENT_PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. While the ID in the PAT_ID column will get cleared out when its variant record is superseded, the value in this column will continue to indicate the patient. |
| 56 | `PERSISTENT_RQG_GROUPER_ID` | NUMERIC |  | The historically maintained requisition grouper ID. While the requisition grouper ID in item 99 will be cleared out of a VAR record when a new VAR superscedes it, this will retain the grouper link. |
| 57 | `PGX_DRUG_TXPORT_C_NAME` | VARCHAR |  | Predicted phenotype for drug efficacy through drug transport mechanism. |
| 58 | `PGX_ACT_SCORE_LOWER` | NUMERIC |  | The lower bound of the activity score on the pharmacogenomic variant. If the activity score is a value and not a range, this will have the same value as PGX_ACT_SCORE_UPPER. If the activity score is a range without a lower bound specified, this column will contain 0. |
| 59 | `PGX_ACT_SCORE_UPPER` | NUMERIC |  | The upper bound of the activity score on the pharmacogenomic variant. If the activity score is a value and not a range, this will have the same value as PGX_ACT_SCORE_LOWER. If the activity score is a range without an upper bound specified, this column will contain 99999. |
| 60 | `DISPLAY_NAME` | VARCHAR |  | The name used when the variant is displayed |
| 61 | `ISCN_NAME` | VARCHAR |  | The ISCN name assigned to the variant. |
| 62 | `COPY_NUMBER_LOWER` | NUMERIC |  | Lower bound for the copy number of a variant. |
| 63 | `COPY_NUMBER_UPPER` | NUMERIC |  | Upper bound for the copy number of a variant. |
| 64 | `VARIANT_FINDING_TYPE_C_NAME` | VARCHAR |  | Stores whether the variant represents an incidental finding. |
| 65 | `AFFECTED_EXON_START` | INTEGER |  | The lowest exon number affected by the variant |
| 66 | `AFFECTED_EXON_END` | INTEGER |  | The highest exon number affected by the variant |
| 67 | `AFFECTED_INTRON_START` | INTEGER |  | The lowest intron number affected by the variant |
| 68 | `AFFECTED_INTRON_END` | INTEGER |  | The highest intron number affected by the variant |
| 69 | `STDRD_AMINO_ACID_CHANGE` | VARCHAR |  | Parsed amino acid change based off of the original amino acid change string |
| 70 | `CMPT_VARIANT_MOLEC_CONSEQ_C_NAME` | VARCHAR |  | Molecular consequence to be inferred from parsed amino acid change |
| 71 | `CMPT_AMINO_ACID_START_CODON` | INTEGER |  | Start position of amino acid change |
| 72 | `CMPT_AMINO_ACID_END_CODON` | INTEGER |  | End position of amino acid change |
| 73 | `CMPT_AMINO_ACID_REFERENCE` | VARCHAR |  | Reference amino acid that the amino acid changed "from" |
| 74 | `CMPT_AMINO_ACID_ALTERNATE` | VARCHAR |  | Alternate amino acid that the amino acid changed "to" |
| 75 | `CLONAL_HEMAT_C_NAME` | VARCHAR |  | The category number for the association with clonal hematopoiesis. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 76 | `STDRD_TRANSCRIPT_REF_SEQ` | VARCHAR |  | The transcript reference sequence the system validates based off of the lab-provided transcript, protein, and genomic reference sequence values. Follows either the NCBI or EMBL standard. |
| 77 | `STDRD_GENOMIC_REF_SEQ` | VARCHAR |  | The genomic reference sequence the system validates based off of the lab-provided transcript, protein, and genomic reference sequence values. Follows either the NCBI or EMBL standard. |
| 78 | `STDRD_PROTEIN_REF_SEQ` | VARCHAR |  | The protein reference sequence the system validates based off of the lab-provided transcript, protein, and genomic reference sequence values. Follows either the NCBI or EMBL standard. |
| 79 | `TOTAL_REPEAT_NUM_LOWER` | INTEGER |  | The lower bound of the sum of all repeat numbers for a repeat expansion variant. |
| 80 | `TOTAL_REPEAT_NUM_UPPER` | INTEGER |  | The upper bound of the sum of all repeat numbers for a repeat expansion variant. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GENE_ID` | [GENE_IDENT](GENE_IDENT.md) | sole_pk | high |
| `PERSISTENT_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

## Joined in — referenced by (18)

| From | Column | Confidence |
|------|--------|------------|
| [GNOM_INTPRT_VARIANTS](GNOM_INTPRT_VARIANTS.md) | `VARIANT_ID` | high |
| [INDICATOR_REL_ORD_VARIANT](INDICATOR_REL_ORD_VARIANT.md) | `VARIANT_ID` | high |
| [ORD_VARIANT](ORD_VARIANT.md) | `VARIANT_ID` | high |
| [RESULT_VARIANT](RESULT_VARIANT.md) | `VARIANT_ID` | high |
| [VARIANT_GENES](VARIANT_GENES.md) | `VARIANT_ID` | high |
| [VARIANT_HT_AUDIT](VARIANT_HT_AUDIT.md) | `VARIANT_ID` | high |
| [VARIANT_SKEW](VARIANT_SKEW.md) | `VARIANT_ID` | high |
| [VARIANT_SKEW_VALUE](VARIANT_SKEW_VALUE.md) | `VARIANT_ID` | high |
| [VARIANT_SYSTEM](VARIANT_SYSTEM.md) | `VARIANT_ID` | high |
| [VAR_ALLELE_NAME](VAR_ALLELE_NAME.md) | `VARIANT_ID` | high |
| [VAR_CONTAINED](VAR_CONTAINED.md) | `VARIANT_ID` | high |
| [VAR_FUSED](VAR_FUSED.md) | `VARIANT_ID` | high |
| [VAR_INTERPRETATION](VAR_INTERPRETATION.md) | `VARIANT_ID` | high |
| [VAR_PGX_MED_USE](VAR_PGX_MED_USE.md) | `VARIANT_ID` | high |
| [VAR_PGX_MED_USE_NARR](VAR_PGX_MED_USE_NARR.md) | `VARIANT_ID` | high |
| [VAR_PHENOTYPES](VAR_PHENOTYPES.md) | `VARIANT_ID` | high |
| [VAR_PHENOTYPE_DESC](VAR_PHENOTYPE_DESC.md) | `VARIANT_ID` | high |
| [VAR_REPEAT_EXPANSION](VAR_REPEAT_EXPANSION.md) | `VARIANT_ID` | high |

