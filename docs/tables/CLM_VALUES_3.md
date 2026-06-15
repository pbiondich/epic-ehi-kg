# CLM_VALUES_3

> All values associated with a claim are stored in the Claim External Value record. The CLM_VALUES_3 table holds claim level values set by the system during claims processing or by user edits.

**Overflow of:** [CLM_VALUES](CLM_VALUES.md)  
**Primary key:** `RECORD_ID`  
**Columns:** 50

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim values record. |
| 2 | `ASST_SURG_NAM_SUF` | VARCHAR |  | The suffix to the assistant dental surgeon's name. |
| 3 | `ASST_SURG_NPI` | VARCHAR |  | The assistant dental surgeon's National Provider Identifier (NPI). |
| 4 | `ASST_SURG_TAXONOMY` | VARCHAR |  | The assistant dental surgeon's taxonomy code. |
| 5 | `SVC_FAC_NAM` | VARCHAR |  | The name of the external location where the services were performed. |
| 6 | `SVC_FAC_NPI` | VARCHAR |  | The NPI of the external location where the services were performed. |
| 7 | `SVC_FAC_CNCT_NAM` | VARCHAR |  | The contact name for the external location. |
| 8 | `SVC_FAC_CNCT_PH` | VARCHAR |  | The contact phone number for the external location. |
| 9 | `SVC_FAC_CNCT_EXT` | VARCHAR |  | The contact phone extension for the external location. |
| 10 | `SVC_FAC_ADDR_1` | VARCHAR |  | The first line of the external location street address. |
| 11 | `SVC_FAC_ADDR_2` | VARCHAR |  | The second line of the external location street address. |
| 12 | `SVC_FAC_CITY` | VARCHAR |  | The external location's city. |
| 13 | `SVC_FAC_STATE` | VARCHAR |  | The external location's state. |
| 14 | `SVC_FAC_ZIP` | VARCHAR |  | The external location's ZIP code. |
| 15 | `SVC_FAC_CNTRY` | VARCHAR |  | The external location's country. It is only populated if the address is outside the United States. |
| 16 | `SVC_FAC_CNTRY_SUB` | VARCHAR |  | The external location's country subdivision (state, province, etc). It is only populated if the address is outside the United States. |
| 17 | `PICK_UP_ADDR_1` | VARCHAR |  | The first line of the ambulance pick-up location street address. |
| 18 | `PICK_UP_ADDR_2` | VARCHAR |  | The second line of the ambulance pick-up location street address. |
| 19 | `PICK_UP_CITY` | VARCHAR |  | The ambulance pick-up location's city. |
| 20 | `PICK_UP_STATE` | VARCHAR |  | The ambulance pick-up location's state. |
| 21 | `PICK_UP_ZIP` | VARCHAR |  | The ambulance pick-up location's ZIP code. |
| 22 | `PICK_UP_CNTRY` | VARCHAR |  | The ambulance pick-up location's country. It is only populated if the address is outside the United States. |
| 23 | `PICK_UP_CNTRY_SUB` | VARCHAR |  | The ambulance pick-up location's country subdivision (e.g., state, province). It is only populated if the address is outside the United States. |
| 24 | `DROP_OFF_NAM` | VARCHAR |  | The name of the ambulance drop-off location. |
| 25 | `DROP_OFF_ADDR_1` | VARCHAR |  | The first line of the ambulance drop-off location street address. |
| 26 | `DROP_OFF_ADDR_2` | VARCHAR |  | The second line of the ambulance drop-off location street address. |
| 27 | `DROP_OFF_CITY` | VARCHAR |  | The ambulance drop-off location's city. |
| 28 | `DROP_OFF_STATE` | VARCHAR |  | The ambulance drop-off location's state. |
| 29 | `DROP_OFF_ZIP` | VARCHAR |  | The ambulance drop-off location's ZIP code. |
| 30 | `DROP_OFF_CNTRY` | VARCHAR |  | The ambulance drop-off location's country. It is only populated if the address is outside the United States. |
| 31 | `DROP_OFF_CNTRY_SUB` | VARCHAR |  | The ambulance drop-off location's country subdivision (e.g., state, province). It is only populated if the address is outside the United States. |
| 32 | `CREATE_DT` | DATETIME |  | The date the claim was created. It is used for paper institutional claims. |
| 33 | `CLM_CVG_AMT_PAID` | NUMERIC |  | The amount already paid by the payer of the current coverage. |
| 34 | `PAT_PROP_CAS_ID_TYP` | VARCHAR |  | The qualifier for the Property and Casualty Patient ID used on American National Standards Institute (ANSI) version 5010 claims. |
| 35 | `PAT_PROP_CAS_ID` | VARCHAR |  | This column stores the patient identifier for property and casualty claims used on American National Standards Institute (ANSI) version 5010 claims. |
| 36 | `ADMSN_QUAL` | VARCHAR |  | The qualifier to identify when the admission hour is reported along with the admission date. |
| 37 | `REMARK` | VARCHAR |  | The claim remark printed on institutional claims as the billing note. |
| 38 | `CLM_CVG_AMT_DUE` | NUMERIC |  | The amount due by the payer of the current coverage. |
| 39 | `CLM_CVG_COMPLMT_ID` | VARCHAR |  | The complementary payer ID for the payer of the current coverage. |
| 40 | `CLM_CVG_REL_INFO_DT` | DATETIME |  | The date on which the insured authorized the release of information to the payer. |
| 41 | `LOCAL_USE_CMS` | VARCHAR |  | The value to print in Reserved for Local Use Box 10d on the paper 1500 version 08/05 Centers for Medicare and Medicaid Services (CMS) claim form. On the 1500 version 02/12 form, this field was removed and no longer used. |
| 42 | `DISABILITY_QUAL` | VARCHAR |  | The qualifier for the disability date and time. |
| 43 | `DISABILITY_TM_QUAL` | VARCHAR |  | The disability time format qualifier. |
| 44 | `CAS_SRC_CEV_ID` | NUMERIC |  | The source claim values record to which this reason code claim values record is attached. |
| 45 | `CAS_LVL_C_NAME` | VARCHAR |  | The indicator that the claim values record includes claim-level or line-level explanation of benefits data. |
| 46 | `CAS_CVG_LN_NUM` | INTEGER |  | The coverage line number in the source claim values record for claim-level explanation of benefits. |
| 47 | `CAS_SVC_LN_NUM` | INTEGER |  | The service line number in the source claim values record. |
| 48 | `NCPDP_RECORD_TYPE` | VARCHAR |  | The National Council for Prescription Drug Programs (NCPDP) transaction type being submitted. |
| 49 | `TXST_TRANSMISSION_ACTION` | VARCHAR |  | The indicator that the file being loaded is a replacement file, update file, or delete file. |
| 50 | `TXST_SUBMISSION_NUMBER` | VARCHAR |  | The number of times data set has been re-sent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

