# RES_MICRO_CULTURE

> This table contains information about microbiology culture results.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 19  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CULTURE_GENUS_C_NAME` | VARCHAR | org | The genus of an organism. This is a low-level taxonomic rank used in the biological classification of organisms |
| 4 | `CULTURE_REPORT_ORG_YN` | VARCHAR |  | Indicates whether or not an organism should be reported. Y indicates that the organism will be reported. A null value or an N indicates that the organism will not be reported. |
| 5 | `CULTURE_SPECIES_C_NAME` | VARCHAR | org | The species of an organism. Species are the basic taxonomic units of biological classification. |
| 6 | `CULTURE_QUANTITY_C_NAME` | VARCHAR | org | Quantity of bacteria found |
| 7 | `CULTURE_ORG_WRKCD_ID` | VARCHAR |  | The unique ID of the organism workcard. |
| 8 | `CULTURE_CFU_QNTY` | VARCHAR |  | Enter the quantity of bacteria found |
| 9 | `BACT_UNITS_C_NAME` | VARCHAR | org | The bacterial units category number for the isolate. |
| 10 | `CULTURE_ABNRML_C_NAME` | VARCHAR | org | Abnormality of the organism |
| 11 | `CUR_ACTION_ID` | NUMERIC |  | The current workcard action for each isolate. |
| 12 | `CUR_ACTION_ID_RECORD_NAME` | VARCHAR |  | The name of the node record. |
| 13 | `CULT_ORG_ID` | NUMERIC |  | The unique record ID of the organism that was identified on this line of the result. |
| 14 | `CULT_ORG_ID_NAME` | VARCHAR |  | The name of the organism. |
| 15 | `CULT_RSLTD_INS_DTTM` | DATETIME (Local) |  | The isolate result instant received from an instrument interface or from manual result entry. |
| 16 | `USR_OVRD_CUL_REP_ID` | VARCHAR |  | The unique ID associated with the user record responsible for overriding reportable flag of an organism. This column is frequently used to link to the CLARITY_EMP table. |
| 17 | `USR_OVRD_CUL_REP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 18 | `CULT_INSTR_PROF_IDENT` | VARCHAR |  | Stores the network concept identifier associated with the isolate's resulting method at the time of resulting or verification. |
| 19 | `ORGANISM_TXT_BACT` | VARCHAR |  | Stores free text organsim pre-comments. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

