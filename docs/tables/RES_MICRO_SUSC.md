# RES_MICRO_SUSC

> This table contains susceptibility results, including antibiotics and interpretations. RES_MICRO_CULTURE can be linked to this table by linking RES_MICRO_SUSC.CULTURE_ID to RES_MICRO_CULTURE.RESULT_ID and RES_MICRO_SUSC.UNIQUE_ORGANISM_ID to RES_MICRO_CULTURE.LINE.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 16  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SUSC_ANTIBIOTIC_ID` | NUMERIC |  | The component being tested |
| 4 | `SUSC_ANTIBIOTIC_ID_NAME` | VARCHAR |  | The name of the component. |
| 5 | `SUSC_VALUE` | VARCHAR |  | The value for this component |
| 6 | `SUSC_ANTI_UNITS_C_NAME` | VARCHAR | org | Stores the antibiotic unit |
| 7 | `SUSC_INTERPRETATN_C_NAME` | VARCHAR | org | Holds the antibiotic's susceptibility interpretation. |
| 8 | `SUSC_TEST_METH_ID` | VARCHAR |  | The testing method for this component |
| 9 | `SUSC_TEST_METH_ID_METHOD_NAME` | VARCHAR |  | The name of the instrument interface, method, method grouper, or middle tier interface record. |
| 10 | `SUSC_ANTI_CMT_C_NAME` | VARCHAR | org | Item to store category-based antibiotic comments. This data is moved to Component multiline user comment pointer (OVR-51202) and Multiline user comment storage (OVR-52202). |
| 11 | `SUSC_REPORTED_C_NAME` | VARCHAR |  | The category number that indicates whether the component is reported for this result. |
| 12 | `UNIQUE_ORGANISM_ID` | INTEGER |  | A number used to uniquely identify the organism this susceptibility test is for. To retrieve information about the associated organism, join RES_MICRO_SUSC.UNIQUE_ORGANISM_ID with RES_MICRO_CULTURE.LINE and RES_MICRO_SUSC.CULTURE_ID with RES_MICRO_CULTURE.RESULT_ID. |
| 13 | `CULTURE_ID` | VARCHAR |  | The unique ID of the associated culture test's current result record. |
| 14 | `SUSC_MTD_LNC_ID_LNC_LONG_NAME` | VARCHAR |  | The more readable format than the fully specified name in Logical Observation Identifiers Names and Codes (LOINC®) code. |
| 15 | `COMP_ACCREDITED_YN` | VARCHAR |  | This item determines the accreditation status of the corresponding component. If set to Y-Yes, the corresponding component is accredited. If set to N-No, the corresponding component is not accredited. If null, no evaluation was performed on the component to determine if it is accredited or not. |
| 16 | `SUSC_INSTR_PROF_IDENT` | VARCHAR |  | Stores the network concept identifier associated with the component's resulting method at the time of resulting or verification. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

