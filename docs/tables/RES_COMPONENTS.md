# RES_COMPONENTS

> Primary table for result component information.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 47  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier of the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMPONENT_ID` | NUMERIC | shared | Internal component ID |
| 4 | `COMPONENT_ID_NAME` | VARCHAR |  | The name of the component. |
| 5 | `COMPONENT_RESULT` | VARCHAR |  | Component result interpreted value |
| 6 | `COMPONENT_VALUE` | VARCHAR |  | Component result value |
| 7 | `COMPONENT_UNITS` | VARCHAR |  | Component result units |
| 8 | `COMPONENT_ABN_C_NAME` | VARCHAR | org | Component abnormal category value |
| 9 | `COMPONENT_DELTA_YN_NAME` | VARCHAR |  | If this value is 1 (true), it indicates that a delta has occurred for this component. |
| 10 | `COMPONENT_NRML_LO` | VARCHAR |  | This item specifies the lowest "normal" value for this component if applicable. |
| 11 | `COMPONENT_NRML_HI` | VARCHAR |  | This item specifies the highest "normal" value for this component, if applicable. |
| 12 | `COMPONENT_CMT` | VARCHAR |  | This item allows entry of a free-text comment related specifically to this component. |
| 13 | `COMPONENT_MTHD_ID` | VARCHAR |  | The testing method for this component. |
| 14 | `COMPONENT_MTHD_ID_METHOD_NAME` | VARCHAR |  | The name of the instrument interface, method, method grouper, or middle tier interface record. |
| 15 | `COMPONENT_RANGE` | VARCHAR |  | The normal range for the component or a list of values that are considered normal. |
| 16 | `COMPONENT_INST` | DATETIME (Local) |  | The instant the component was resulted. |
| 17 | `COMPONENT_LAB_ID_LAB_NAME` | VARCHAR |  | The name of the lab record. |
| 18 | `COMPONENT_REPORT_YN_NAME` | VARCHAR |  | This item indicates whether or not a component should be reported. |
| 19 | `COMPON_DILUTION` | VARCHAR |  | The factor by which the value is diluted |
| 20 | `COMPON_LINEAR_YN` | VARCHAR |  | The linearity flag for this component |
| 21 | `COMPON_RPT_SET_BY_C_NAME` | VARCHAR |  | Indicates how the report flag for this component was determined |
| 22 | `COMPON_REPORTABLE_C_NAME` | VARCHAR |  | The reportable (notifiable) flag for this component |
| 23 | `COMP_VAL_STAT_C_NAME` | VARCHAR |  | The validation status category number for this component. |
| 24 | `COMP_VERIF_STATUS_C_NAME` | VARCHAR |  | The verification status category number for this component. |
| 25 | `COMP_VERIF_LAB_ID_LAB_NAME` | VARCHAR |  | The name of the lab record. |
| 26 | `COMP_VERIF_USER_ID` | VARCHAR |  | The unique ID of the user who verified the component. |
| 27 | `COMP_VERIF_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 28 | `USR_OVRD_ABNRML_ID` | VARCHAR |  | The unique ID associated with the user record responsible for overriding abnormality or reference range. This column is frequently used to link to the CLARITY_EMP table. |
| 29 | `USR_OVRD_ABNRML_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 30 | `USR_OVRD_REP_FLG_ID` | VARCHAR |  | The unique ID associated with the user record responsible for overriding the reportable flag. This column is frequently used to link to the CLARITY_EMP table. |
| 31 | `USR_OVRD_REP_FLG_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 32 | `OVRIDE_ABNRML_YN` | VARCHAR |  | Indicates whether users can override the reference range or abnormality from Result Entry. |
| 33 | `OVRIDE_REP_FLAG_YN` | VARCHAR |  | Indicates whether users can override the reportable flag from Result Entry. |
| 34 | `CMP_VERIF_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant in UTC at which the component on the corresponding line was verified. |
| 35 | `COMP_LNC_RECORD_ID_LNC_LONG_NAME` | VARCHAR |  | The more readable format than the fully specified name in Logical Observation Identifiers Names and Codes (LOINC®) code. |
| 36 | `COMP_ACCREDITED_YN` | VARCHAR |  | This item determines the accreditation status of the corresponding component. If set to Y-Yes, the corresponding component is accredited. If set to N-No, the corresponding component is not accredited. If null, no evaluation was performed on the component to determine if it is accredited or not. |
| 37 | `COMP_UNCERTAIN_MEAS` | VARCHAR |  | The extent to which a given value is uncertain (e.g. if the uncertainty percentage is 5%, then the component uncertainty value for a result of 1.00 will be +/- 0.05). NOTE: This is how the data is stored in the database; as string format. This field stores numeric in M internal format, using a period as the decimal separator irrespective of locale. |
| 38 | `COMP_NETWORK_CONCEPT_IDENT` | VARCHAR |  | Stores the network concept identifier associated with this component at the time of resulting. |
| 39 | `COMP_DISP_RANGE_SET_BY_C_NAME` | VARCHAR |  | Records what set the display reference range. |
| 40 | `COMP_INSTR_PROF_IDENT` | VARCHAR |  | Stores the network concept identifier associated with the component's resulting method at the time of resulting or verification. |
| 41 | `COMPON_TAG_LN` | INTEGER |  | Line number for the tested against group relevant to this row, indicating that all component lines pointing to the same line should be grouped together logically. |
| 42 | `CMP_ADD_USER_ID` | VARCHAR |  | User who added the component to the test |
| 43 | `CMP_ADD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 44 | `CMP_ADD_DTTM` | DATETIME (Attached) |  | Stores the local instant of when the component was originally added to the test. |
| 45 | `CMP_ADD_UTC_DTTM` | DATETIME (UTC) |  | Stores the UTC instant of when the component was originally added to the test. |
| 46 | `COMP_NORM_LO_INEQ_C_NAME` | VARCHAR |  | Stores inequalities associated with component normal low (I OVR 51040). |
| 47 | `COMP_NORM_HI_INEQ_C_NAME` | VARCHAR |  | Stores inequalities associated with component normal high (I OVR 51045). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

