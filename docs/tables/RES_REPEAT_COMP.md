# RES_REPEAT_COMP

> This table is used to extract information on component-level repeats.

**Overflow family:** [RES_REPEAT_COMP_2](RES_REPEAT_COMP_2.md)  
**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 54  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RPT_COMP_ID` | NUMERIC |  | The unique ID associated with the repeat component. |
| 4 | `RPT_COMP_ID_NAME` | VARCHAR |  | The name of the component. |
| 5 | `RPT_SELECT_YN_NAME` | VARCHAR |  | Indicates whether a repeat component was selected. |
| 6 | `RPT_COMP_VALUE` | VARCHAR |  | Repeat component value |
| 7 | `RPT_ORIG_VALUE` | VARCHAR |  | Repeat component original value |
| 8 | `RPT_COMP_UNITS` | VARCHAR |  | Repeat component units |
| 9 | `RPT_ABNORMAL_C_NAME` | VARCHAR | org | Repeat component abnormal value |
| 10 | `RPT_DELTA_YN_NAME` | VARCHAR |  | Repeat component delta |
| 11 | `RPT_NORM_LOW` | VARCHAR |  | Repeat component normal low value |
| 12 | `RPT_NORM_HIGH` | VARCHAR |  | Repeat component normal high value |
| 13 | `RPT_COMMENT` | VARCHAR |  | Repeat component comment |
| 14 | `RPT_METHOD_ID` | VARCHAR |  | Repeat component method |
| 15 | `RPT_METHOD_ID_METHOD_NAME` | VARCHAR |  | The name of the instrument interface, method, method grouper, or middle tier interface record. |
| 16 | `RPT_NORM_RANGE` | VARCHAR |  | The normal range for the repeat component or a list of values that are considered normal. |
| 17 | `RPT_VAL_STATUS_C_NAME` | VARCHAR |  | The repeat component validation status category number for the repeat component. |
| 18 | `RPT_RES_INSTANT` | DATETIME |  | Repeat component resulting instant |
| 19 | `RPT_RES_LAB_ID_LAB_NAME` | VARCHAR |  | The name of the lab record. |
| 20 | `RPT_VER_STAT_C_NAME` | VARCHAR |  | Repeat component verification status |
| 21 | `RPT_VER_INSTANT` | DATETIME |  | Repeat component verification instant |
| 22 | `RPT_VER_LAB_ID_LAB_NAME` | VARCHAR |  | The name of the lab record. |
| 23 | `RPT_VER_USER_ID` | VARCHAR |  | Repeat component verification user |
| 24 | `RPT_VER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 25 | `IS_RPT_REPORTD_YN_NAME` | VARCHAR |  | Flags whether or not repeat component is reported |
| 26 | `RPT_INTERPRET_C_NAME` | VARCHAR | org | Repeat component interpretation |
| 27 | `RPT_AB_UNITS_C_NAME` | VARCHAR | org | Repeat component antibiotic units |
| 28 | `RPT_AB_COMMENTS_C_NAME` | VARCHAR | org | The antibiotic comment category number for the repeat antibiotic component. |
| 29 | `RPT_RFLX_ACTIONS` | VARCHAR |  | Repeat component reflex actions fired |
| 30 | `RPT_CAL_COM_RFLX_R` | VARCHAR |  | Repeat calculated component reflex reasons |
| 31 | `RPT_COMP_RESULT` | VARCHAR |  | Repeat component result |
| 32 | `REPEAT_COMP_DILUTE` | VARCHAR |  | The factor by which the value is diluted for each component repeat. |
| 33 | `REPEAT_LINEARITY_YN` | VARCHAR |  | The linearity flag for this component repeat. |
| 34 | `REPEAT_RPT_SET_BY_C_NAME` | VARCHAR |  | Indicates how the report flag for this component was determined |
| 35 | `REP_CMP_REV_TYP_C_NAME` | VARCHAR |  | Records the type of cytology review performed for a given result. |
| 36 | `RPT_EDITING_USER_ID` | VARCHAR |  | The user that resulted the related repeat component. |
| 37 | `RPT_EDITING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 38 | `REPEAT_INTERP_SET_C_NAME` | VARCHAR |  | Indicates how the interpretation for this component was determined. |
| 39 | `USR_OVRD_ABNL_ID` | VARCHAR |  | The unique ID associated with the user record. This column is frequently used to link to the CLARITY_EMP table. Records the user responsible for overriding abnormality or reference range for this component repeat. |
| 40 | `USR_OVRD_ABNL_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 41 | `USR_OVRD_RPT_FLG_ID` | VARCHAR |  | The unique ID associated with the user record. This column is frequently used to link to the CLARITY_EMP table. Records the user responsible for overriding the reportable flag for this component repeat. |
| 42 | `USR_OVRD_RPT_FLG_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 43 | `REPEAT_RES_UTC_DTTM` | DATETIME (UTC) |  | The instant when the repeat was resulted in UTC. |
| 44 | `RPT_VERIF_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant in UTC at which the component repeat on the corresponding line was verified. |
| 45 | `REPEAT_REPORTABLE_C_NAME` | VARCHAR |  | The reportable category ID for the component repeat. |
| 46 | `RPT_LNC_ID_LNC_LONG_NAME` | VARCHAR |  | The more readable format than the fully specified name in Logical Observation Identifiers Names and Codes (LOINC®) code. |
| 47 | `RPT_SUSC_MTD_LNC_ID_LNC_LONG_NAME` | VARCHAR |  | The more readable format than the fully specified name in Logical Observation Identifiers Names and Codes (LOINC®) code. |
| 48 | `REPEAT_COMP_ACCR_YN` | VARCHAR |  | This item determines the accreditation status of the corresponding component repeat. If set to Y-Yes, the corresponding component repeat is accredited. If set to N-No, the corresponding component repeated is not accredited. If null, no evaluation was performed on the component repeat to determine if it is accredited or not. |
| 49 | `REPEAT_UNCERTAINTY` | VARCHAR |  | The extent to which a given value is uncertain (e.g. if the uncertainty percentage is 5%, then the repeat uncertainty value for a result of 1.00 will be +/- 0.05). NOTE: This is how the data is stored in the database; as string format. This field stores numeric in M internal format, using a period as the decimal separator irrespective of locale. |
| 50 | `RPT_NETWORK_CONCEPT_IDENT` | VARCHAR |  | Copy of OVR-51299 for each repeat of the component. Stores the network concept identifier associated with this component at the time of resulting. |
| 51 | `RPT_COMP_DISP_RANGE_SET_BY_C_NAME` | VARCHAR |  | Records what set the display reference range. |
| 52 | `REP_INSTR_PROF_IDENT` | VARCHAR |  | Stores the network concept identifier associated with the repeat component's resulting method at the time of resulting or verification. |
| 53 | `RPT_NORM_LO_INEQ_C_NAME` | VARCHAR |  | Stores inequalities associated with repeat component normal low (I OVR 53040). |
| 54 | `RPT_NORM_HI_INEQ_C_NAME` | VARCHAR |  | Stores inequalities associated with component normal high (I OVR 53045). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

